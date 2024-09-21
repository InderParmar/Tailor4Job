import click
import os
import sys
from utils import process_files, generate_output
from dotenv import load_dotenv
 
load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv('GROQ_API_KEY')
 
@click.command()
@click.option('--version', '-v', is_flag=True, help='Prints the tool’s name and current version.')
@click.option('--model', '-m', default='llama3-8b-8192', help='Specify the model to use.')
@click.option('--output', '-o', default=None, help='Specify an output filename.')
@click.option('--analysis_mode', '-a', type=click.Choice(['basic', 'detailed'], case_sensitive=False), default='detailed', help='Choose between basic or detailed analysis.')
@click.option('--token-usage', '-t', is_flag=True, help='Show token usage information.')
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def main(version, model, output, files, analysis_mode, token_usage):
    if version:
        click.echo("Tailor4Job Version 0.1", err=False)  # Normal output to stdout
        sys.exit(0)
 
    if not files:
        click.echo('No input files provided. Use --help for usage information.', err=True)  # Error to stderr
        sys.exit(1)
 
    try:
        # Debug information about the files being processed
        click.echo(f"Processing files: {files}", err=True)  # Send debug info to stderr
 
        # Process input files and generate tailored output
        tailored_content, token_info = process_files(files, API_KEY, model, analysis_mode, token_usage)
 
        # Debug information about the generated content
        click.echo("Processing completed successfully", err=True)  # Send debug info to stderr
 
        # Show token usage information if flag is set
        if token_usage and token_info:
            click.echo(f"Prompt Tokens: {token_info['prompt_tokens']}\nCompletion Tokens: {token_info['completion_tokens']}\nTotal Tokens: {token_info['total_tokens']}", err=True)
 
        # Generate output based on file format
        if output:
            generate_output(tailored_content, output)
            click.echo(f"Output saved to {output}", err=True)  # Debug info to stderr
        else:
            click.echo(tailored_content)  # Output to stdout (normal output)
 
    except Exception as e:
        click.echo(f'Error: {e}', err=True)  # Send error messages to stderr
        sys.exit(1)
 
 
if __name__ == '__main__':
    main()