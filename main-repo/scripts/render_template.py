import os
from jinja2 import Environment, FileSystemLoader

def main():
    # Get environment variables
    template_path = os.environ['TEMPLATE_PATH']
    output_file = os.environ['OUTPUT_FILE']
    github_repo = os.environ['GITHUB_REPO']
    git_tag = os.environ['GIT_TAG']
    file_sha = os.environ['FILE_SHA']

    # Configure Jinja environment
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    template = env.get_template(os.path.basename(template_path))

    # Render template and write output
    with open(output_file, 'w') as f:
        f.write(template.render(
            github_repo=github_repo,
            git_tag=git_tag,
            file_sha=file_sha
        ))

if __name__ == '__main__':
    main()
