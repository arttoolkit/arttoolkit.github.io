import os
import yaml
import json
import frontmatter

def yaml_to_json(yaml_content):
    json_content = json.dumps(yaml_content, indent=2)
    return json_content

def convert_files_to_json(folder_path, output_json_path):
    all_json_data = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, 'r', encoding='utf-8') as md_file:
                md_content = frontmatter.load(md_file)
                md_content.metadata['name'] = os.path.splitext(os.path.basename(file_path))[0]
                yaml_content = md_content.metadata

                json_content = json.loads(yaml_to_json(yaml_content))
                all_json_data.append(json_content)

    with open(output_json_path, 'w') as output_json_file:
        json.dump(all_json_data, output_json_file, indent=2)

if __name__ == "__main__":
    folder_path = './../_wadcoms'
    output_json_path = './redcoms.json'

    convert_files_to_json(folder_path, output_json_path)
