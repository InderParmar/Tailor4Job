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
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def main(version, model, output, files):
    if version:
        click.echo("Tailor4Job Version 0.1")
        sys.exit(0)

    if not files:
        click.echo('No input files provided. Use --help for usage information.', err=True)
        sys.exit(1)

    try:
        # Process input files and generate tailored output
        tailored_content = process_files(files, API_KEY, model)

        # Generate output based on file format
        if output:
            generate_output(tailored_content, output)
        else:
            click.echo(tailored_content)  # Output to stdout

    except Exception as e:
        click.echo(f'Error: {e}', err=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
