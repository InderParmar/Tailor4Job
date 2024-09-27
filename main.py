import click
import os
import sys
from utils import process_files, generate_output
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('GROQ_API_KEY')

@click.command()
@click.option('--version', '-v', is_flag=True, help='Prints the tool’s name and current version.')
@click.option('--model', '-m', default='llama3-8b-8192', help='Specify the model(s) to use, comma-separated for multiple models.')
@click.option('--output', '-o', default=None, help='Specify an output filename (base name for multiple models).')
@click.option('--analysis_mode', '-a', type=click.Choice(['basic', 'detailed'], case_sensitive=False), default='detailed', help='Choose between basic or detailed analysis.')
@click.option('--token-usage', '-t', is_flag=True, help='Show token usage information.')
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def main(version, model, output, files, analysis_mode, token_usage):
    if version:
        click.echo("Tailor4Job Version 0.1", err=False)
        sys.exit(0)

    if not files:
        click.echo('No input files provided. Use --help for usage information.', err=True)
        sys.exit(1)

    try:
        # Split the model string into a list of models
        models = model.split(',')

        # Process files for each model and collect results
        results = process_files(files, API_KEY, models, analysis_mode, token_usage)

        # Generate output for each model
        for model_name, (content, token_info) in results.items():
            if output:
                output_filename = f"{output}_{model_name}.docx"
                generate_output(content, output_filename)
                click.echo(f"Output saved to {output_filename}", err=True)
            else:
                click.echo(content)

            # Show token usage information if flag is set
            if token_usage and token_info:
                click.echo(f"Prompt Tokens: {token_info['prompt_tokens']}\nCompletion Tokens: {token_info['completion_tokens']}\nTotal Tokens: {token_info['total_tokens']}", err=True)

    except Exception as e:
        click.echo(f'Error: {e}', err=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
