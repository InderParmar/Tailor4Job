import click
import os
import sys
from dotenv import load_dotenv
from utils import process_files, generate_output

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
# Ensure API key is not None or empty
if not OPENROUTER_API_KEY:
    raise Exception("OpenRouter API key is missing. Make sure it's set in the .env file.")

@click.command()
@click.option('--version', '-v', is_flag=True, help='Prints the tool’s name and current version.')
@click.option('--model', '-m', default='llama3-8b-8192', help='Specify the model to use.')
@click.option('--provider', '-p', default='groq', help='Specify the provider to use (groq or openrouter).')
@click.option('--output', '-o', default=None, help='Specify an output filename.')
@click.option('--analysis_mode', '-a', type=click.Choice(['basic', 'detailed'], case_sensitive=False), default='detailed', help='Choose between basic or detailed analysis.')
@click.option('--token-usage', '-t', is_flag=True, help='Show token usage information.')
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def main(version, model, provider, output, files, analysis_mode, token_usage):
    if version:
        click.echo("Tailor4Job Version 0.1", err=False)
        sys.exit(0)

    if not files:
        click.echo('No input files provided. Use --help for usage information.', err=True)
        sys.exit(1)

    try:
        # Debug information about the provider and files being processed
        click.echo(f"Processing files using {provider} provider", err=True)

        # Select the appropriate API key based on the provider
        if provider == 'groq':
            api_key = GROQ_API_KEY
        elif provider == 'openrouter':
            api_key = OPENROUTER_API_KEY
        else:
            click.echo(f"Error: Unsupported provider '{provider}'. Please choose 'groq' or 'openrouter'.", err=True)
            sys.exit(1)

        # Process input files and generate tailored content
        tailored_content, token_info = process_files(files, api_key, model, analysis_mode, token_usage, provider)

        # Debug information about the generated content
        click.echo("Processing completed successfully", err=True)

        # Show token usage information if flag is set
        if token_usage and token_info:
            click.echo(f"Prompt Tokens: {token_info['prompt_tokens']}\nCompletion Tokens: {token_info['completion_tokens']}\nTotal Tokens: {token_info['total_tokens']}", err=True)

        # Generate output based on file format
        if output:
            generate_output(tailored_content, output)
            click.echo(f"Output saved to {output}", err=True)
        else:
            click.echo(tailored_content)

    except Exception as e:
        click.echo(f'Error: {e}', err=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
