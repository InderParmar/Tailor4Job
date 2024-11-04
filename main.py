import click
import os
import sys
import toml
from utils import process_files, generate_output
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to get the correct API key based on the provider
def get_api_key(provider_name):
    """Fetch the correct API key based on the provider."""
    if provider_name == 'groq':
        return os.getenv('GROQ_API_KEY')
    elif provider_name == 'openrouter':
        return os.getenv('OPENROUTER_API_KEY')
    else:
        raise Exception(f"Unsupported provider: {provider_name}")

# Path to the TOML config file in the home directory
def load_config():
    """Load the TOML config file from the user's home directory if it exists."""
    try:
        return toml.load(os.path.expanduser("~/.tailor4job_config.toml"))
    except FileNotFoundError:
        return {}
    except toml.TomlDecodeError:
        click.echo("Error: Could not parse TOML config file at ~/.tailor4job_config.toml", err=True)
        sys.exit(1)

# Function to process model and provider pairs
def process_model_provider(model_name, provider_name, files, api_key, analysis_mode, token_usage):
    click.echo(f"Processing files using {model_name} model and {provider_name} provider", err=True)
    tailored_content, token_info = process_files(files, api_key, model_name, analysis_mode, token_usage, provider_name)
    return tailored_content, token_info

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
    model = model or config.get('model')
    provider = provider or config.get('provider')
    analysis_mode = analysis_mode or config.get('analysis_mode')
    output = output or config.get('output')

    try:
        # Split the model and provider strings into lists
        model_name_list = model.split(',')
        provider_name_list = provider.split(',')

        # Check if the number of models matches the number of providers
        if len(model_name_list) != len(provider_name_list):
            click.echo('Error: The number of models must match the number of providers.', err=True)
            sys.exit(1)

        # Loop through each model and provider pair
        for model_name, provider_name in zip(model_name_list, provider_name_list):
            api_key = get_api_key(provider_name)
            tailored_content, token_info = process_model_provider(model_name, provider_name, files, api_key, analysis_mode, token_usage)

            # Sanitize model name for the output filename
            sanitized_model_name = model_name.replace('/', '_').replace(':', '_')

            # Generate a unique output filename for each model
            if output:
                output_filename = f"{sanitized_model_name}_{output}"
                generate_output(tailored_content, output_filename)
                click.echo(f"Output saved to {output_filename}", err=True)
            else:
                click.echo(tailored_content)

            # Show token usage information if flag is set
            if token_usage and token_info:
                click.echo(f"Prompt Tokens: {token_info['prompt_tokens']}\nCompletion Tokens: {token_info['completion_tokens']}\nTotal Tokens: {token_info['total_tokens']}", err=True)

    except Exception as e:
        click.echo(f'Error: {e}', err=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
