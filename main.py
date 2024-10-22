
import click
import os
import sys
import toml
from utils import process_files, generate_output
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')

# Path to the TOML config file in the home directory
def load_config():
    """Load the TOML config file from the user's home directory if it exists."""
    try:
        return toml.load(os.path.expanduser("~/.tailor4job_config.toml"))
    except FileNotFoundError:
        # If the file doesn't exist, just return an empty dict
        return {}
    except toml.TomlDecodeError:
        # If the file exists but is not a valid TOML file
        click.echo(f"Error: Could not parse TOML config file at ~/.tailor4job_config.toml", err=True)
        sys.exit(1)
    return {}

@click.command()
@click.option('--version', '-v', is_flag=True, help='Prints the tool’s name and current version.')
@click.option('--model', '-m', default=None, help='Specify the model(s) to use, comma-separated for multiple models.')
@click.option('--provider', '-p', default=None, help='Specify the provider(s) to use, comma-separated for multiple providers.')
@click.option('--output', '-o', default=None, help='Specify an output filename (base name for multiple models).')
@click.option('--analysis_mode', '-a', type=click.Choice(['basic', 'detailed'], case_sensitive=False), default=None, help='Choose between basic or detailed analysis.')
@click.option('--token-usage', '-t', is_flag=True, help='Show token usage information.')
@click.argument('files', nargs=-1, type=click.Path(exists=True))

def main(version, model, provider, output, files, analysis_mode, token_usage):
    # Load default config from the TOML file if available
    config = load_config()
    print(config)  # Debugging line to see the loaded config
    # If version is requested, print version and exit
    if version:
        click.echo("Tailor4Job Version 0.1", err=False)
        sys.exit(0)

    # If files are not provided as arguments, use files from the config file
    if not files:
        files = config.get('input_files')
        if not files:
            click.echo('No input files provided. Use --help for usage information.', err=True)
            sys.exit(1)

    # Use values from the config file if command-line args are not given
    model = model or config.get('model')  # No default value, loads only from TOML or CLI
    provider = provider or config.get('provider')  # No default value
    analysis_mode = analysis_mode or config.get('analysis_mode')  # No default value
    output = output or config.get('output')  # No default value


    try:
        # Split the model and provider strings into lists
        models = model.split(',')
        providers = provider.split(',')

        # Check if the number of models matches the number of providers
        if len(models) != len(providers):
            click.echo('Error: The number of models must match the number of providers.', err=True)
            sys.exit(1)

        # Loop through each model and provider pair
        for model_name, provider_name in zip(models, providers):
            click.echo(f"Processing files using {model_name} model and {provider_name} provider", err=True)

            # Select the appropriate API key based on the provider
            if provider_name == 'groq':
                api_key = GROQ_API_KEY
            elif provider_name == 'openrouter':
                api_key = OPENROUTER_API_KEY
            else:
                click.echo(f"Error: Unsupported provider '{provider_name}'. Please choose 'groq' or 'openrouter'.", err=True)
                sys.exit(1)

            # Process input files and generate tailored content for each model
            tailored_content, token_info = process_files(files, api_key, model_name, analysis_mode, token_usage, provider_name)

            # Sanitize model name for the output filename (replace '/' and ':' with '_')
            sanitized_model_name = model_name.replace('/', '_').replace(':', '_')

            # Generate a unique output filename for each model
            if output:
                print('Output name processed successfully')

                output_filename = f"{sanitized_model_name}_{output}"
                generate_output(tailored_content, output_filename)
                click.echo(f"Output saved to {output_filename}", err=True)
            else:
                print('Output name not processed successfully')

                click.echo(tailored_content)

            # Show token usage information if flag is set
            if token_usage and token_info:
                click.echo(f"Prompt Tokens: {token_info['prompt_tokens']}\nCompletion Tokens: {token_info['completion_tokens']}\nTotal Tokens: {token_info['total_tokens']}", err=True)

    except Exception as e:
        click.echo(f'Error: {e}', err=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
