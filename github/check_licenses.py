import os
import base64
import csv
import requests
from datetime import datetime

# Read GitHub token from environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    raise Exception("Please set the GITHUB_TOKEN environment variable.")

ORG_NAMES = ['Ferlab-Ste-Justine', 'Ferlab-Ste-Justine-Ops']
CURRENT_YEAR = datetime.now().year
OWNER_NAME = 'Ferlab-Ste-Justine'

APACHE_LICENSE_CONTENT = f"""
Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

"License" shall mean the terms and conditions for use, reproduction,
and distribution as defined by Sections 1 through 9 of this document.

"Licensor" shall mean the copyright owner or entity authorized by
the copyright owner that is granting the License.

"Legal Entity" shall mean the union of the acting entity and all
other entities that control, are controlled by, or are under common
control with that entity. For the purposes of this definition,
"control" means (i) the power, direct or indirect, to cause the
direction or management of such entity, whether by contract or
otherwise, or (ii) ownership of fifty percent (50%) or more of the
outstanding shares, or (iii) beneficial ownership of such entity.

"You" (or "Your") shall mean an individual or Legal Entity
exercising permissions granted by this License.

"Source" form shall mean the preferred form for making modifications,
including but not limited to software source code, documentation
source, and configuration files.

"Object" form shall mean any form resulting from mechanical
transformation or translation of a Source form, including but
not limited to compiled object code, generated documentation,
and conversions to other media types.

"Work" shall mean the work of authorship, whether in Source or
Object form, made available under the License, as indicated by a
copyright notice that is included in or attached to the work
(an example is provided in the Appendix below).

"Derivative Works" shall mean any work, whether in Source or Object
form, that is based on (or derived from) the Work and for which the
editorial revisions, annotations, elaborations, or other modifications
represent, as a whole, an original work of authorship. For the purposes
of this License, Derivative Works shall not include works that remain
separable from, or merely link (or bind by name) to the interfaces of,
the Work and Derivative Works thereof.

"Contribution" shall mean any work of authorship, including
the original version of the Work and any modifications or additions
to that Work or Derivative Works thereof, that is intentionally
submitted to Licensor for inclusion in the Work by the copyright owner
or by an individual or Legal Entity authorized to submit on behalf of
the copyright owner. For the purposes of this definition, "submitted"
means any form of electronic, verbal, or written communication sent
to the Licensor or its representatives, including but not limited to
communication on electronic mailing lists, source code control systems,
and issue tracking systems that are managed by, or on behalf of, the
Licensor for the purpose of discussing and improving the Work, but
excluding communication that is conspicuously marked or otherwise
designated in writing by the copyright owner as "Not a Contribution."

"Contributor" shall mean Licensor and any individual or Legal Entity
on behalf of whom a Contribution has been received by Licensor and
subsequently incorporated within the Work.

2. Grant of Copyright License. Subject to the terms and conditions of
this License, each Contributor hereby grants to You a perpetual,
worldwide, non-exclusive, no-charge, royalty-free, irrevocable
copyright license to reproduce, prepare Derivative Works of,
publicly display, publicly perform, sublicense, and distribute the
Work and such Derivative Works in Source or Object form.

3. Grant of Patent License. Subject to the terms and conditions of
this License, each Contributor hereby grants to You a perpetual,
worldwide, non-exclusive, no-charge, royalty-free, irrevocable
(except as stated in this section) patent license to make, have made,
use, offer to sell, sell, import, and otherwise transfer the Work,
where such license applies only to those patent claims licensable
by such Contributor that are necessarily infringed by their
Contribution(s) alone or by combination of their Contribution(s)
with the Work to which such Contribution(s) was submitted. If You
institute patent litigation against any entity (including a
cross-claim or counterclaim in a lawsuit) alleging that the Work
or a Contribution incorporated within the Work constitutes direct
or contributory patent infringement, then any patent licenses
granted to You under this License for that Work shall terminate
as of the date such litigation is filed.

4. Redistribution. You may reproduce and distribute copies of the
Work or Derivative Works thereof in any medium, with or without
modifications, and in Source or Object form, provided that You
meet the following conditions:

(a) You must give any other recipients of the Work or
Derivative Works a copy of this License; and

(b) You must cause any modified files to carry prominent notices
stating that You changed the files; and

(c) You must retain, in the Source form of any Derivative Works
that You distribute, all copyright, patent, trademark, and
attribution notices from the Source form of the Work,
excluding those notices that do not pertain to any part of
the Derivative Works; and

(d) If the Work includes a "NOTICE" text file as part of its
distribution, then any Derivative Works that You distribute must
include a readable copy of the attribution notices contained
within such NOTICE file, excluding those notices that do not
pertain to any part of the Derivative Works, in at least one
of the following places: within a NOTICE text file distributed
as part of the Derivative Works; within the Source form or
documentation, if provided along with the Derivative Works; or,
within a display generated by the Derivative Works, if and
wherever such third-party notices normally appear. The contents
of the NOTICE file are for informational purposes only and
do not modify the License. You may add Your own attribution
notices within Derivative Works that You distribute, alongside
or as an addendum to the NOTICE text from the Work, provided
that such additional attribution notices cannot be construed
as modifying the License.

You may add Your own copyright statement to Your modifications and
may provide additional or different license terms and conditions
for use, reproduction, or distribution of Your modifications, or
for any such Derivative Works as a whole, provided Your use,
reproduction, and distribution of the Work otherwise complies with
the conditions stated in this License.

5. Submission of Contributions. Unless You explicitly state otherwise,
any Contribution intentionally submitted for inclusion in the Work
by You to the Licensor shall be under the terms and conditions of
this License, without any additional terms or conditions.
Notwithstanding the above, nothing herein shall supersede or modify
the terms of any separate license agreement you may have executed
with Licensor regarding such Contributions.

6. Trademarks. This License does not grant permission to use the trade
names, trademarks, service marks, or product names of the Licensor,
except as required for describing the origin of the Work and
reproducing the content of the NOTICE file.

7. Disclaimer of Warranty. Unless required by applicable law or
agreed to in writing, Licensor provides the Work (and each
Contributor provides its Contributions) on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied, including, without limitation, any warranties or conditions
of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
PARTICULAR PURPOSE. You are solely responsible for determining the
appropriateness of using or redistributing the Work and assume any
risks associated with Your exercise of permissions under this License.

8. Limitation of Liability. In no event and under no legal theory,
whether in tort (including negligence), contract, or otherwise,
unless required by applicable law (such as deliberate and grossly
negligent acts) or agreed to in writing, shall any Contributor be
liable to You for damages, including any direct, indirect, special,
incidental, or consequential damages of any character arising as a
result of this License or out of the use or inability to use the
Work (including but not limited to damages for loss of goodwill,
work stoppage, computer failure or malfunction, or any and all
other commercial damages or losses), even if such Contributor
has been advised of the possibility of such damages.

9. Accepting Warranty or Additional Liability. While redistributing
the Work or Derivative Works thereof, You may choose to offer,
and charge a fee for, acceptance of support, warranty, indemnity,
or other liability obligations and/or rights consistent with this
License. However, in accepting such obligations, You may act only
on Your own behalf and on Your sole responsibility, not on behalf
of any other Contributor, and only if You agree to indemnify,
defend, and hold each Contributor harmless for any liability
incurred by, or claims asserted against, such Contributor by reason
of your accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS

APPENDIX: How to apply the Apache License to your work.

To apply the Apache License to your work, attach the following
boilerplate notice, with the fields enclosed by brackets "[]"
replaced with your own identifying information. (Don't include
the brackets!) The text should be enclosed in the appropriate
comment syntax for the file format. We also recommend that a
file or class name and description of purpose be included on the
same "printed page" as the copyright notice for easier
identification within third-party archives.

Copyright {CURRENT_YEAR} {OWNER_NAME}

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# GitHub API URL
BASE_URL = 'https://api.github.com'
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Function to get all repositories in the organization
def get_org_repositories(org_name):
    repos = []
    page = 1
    while True:
        url = f'{BASE_URL}/orgs/{org_name}/repos?page={page}&per_page=100'
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            raise Exception(f'Error fetching repositories for {org_name}: {response.status_code}')
        page_repos = response.json()
        if not page_repos:
            break
        repos.extend(page_repos)
        page += 1
    return repos

# Function to get the list of known licenses
def get_known_licenses():
    url = 'https://api.github.com/licenses'
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f'Error fetching known licenses: {response.status_code}')
    licenses = response.json()
    return {license['key']: license['name'] for license in licenses}

# Function to check the license of a repository
def check_repo_license(repo, known_licenses):
    repo_name = repo['name']
    org_name = repo['owner']['login']
    is_public = not repo['private']
    url = f'{BASE_URL}/repos/{org_name}/{repo_name}/license'
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        license_info = response.json()
        license_key = license_info['license']['key']
        if license_key in known_licenses:
            license_name = known_licenses[license_key]
            return f"Repository **{repo_name}** in {org_name} has a valid license: {license_name}", 'Valid License', license_name
        else:
            return f"Repository **{repo_name}** in {org_name} has an unrecognized license: {license_key}", 'Unrecognized License', 'Unrecognized'
    elif response.status_code == 404:
        if is_public:
            return f"Repository **{repo_name}** in {org_name} is public and does not have a license file. A license is recommended.", 'No License', 'None'
        else:
            return f"Repository **{repo_name}** in {org_name} is private and does not have a license file. A license is recommended based on internal policy.", 'No License', 'None'
    else:
        return f"Error fetching license for repository **{repo_name}** in {org_name}: {response.status_code}", 'Error', 'Error'


# Function to check if a LICENSE file already exists and its content
def check_license_file_exists(repo):
    repo_name = repo['name']
    org_name = repo['owner']['login']
    url = f'{BASE_URL}/repos/{org_name}/{repo_name}/contents/LICENSE'
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        content = response.json().get('content', '')
        return True, base64.b64decode(content).decode('utf-8')
    return False, ''

# Function to add a license to a repository
def add_license(repo, license_content):
    repo_name = repo['name']
    org_name = repo['owner']['login']
    url = f'{BASE_URL}/repos/{org_name}/{repo_name}/contents/LICENSE'
    data = {
        "message": "Adding Apache License 2.0",
        "content": base64.b64encode(license_content.encode()).decode(),
        "committer": {
            "name": "License Bot",
            "email": "license-bot@example.com"
        }
    }
    response = requests.put(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        return f"Apache License 2.0 added by user to repository **{repo_name}** in {org_name}.", 'Apache License Added'
    elif response.status_code == 403:
        return f"Failed to add Apache License 2.0 to repository **{repo_name}** in {org_name}: 403 Forbidden. Check your token permissions.", 'Add License Failed'
    elif response.status_code == 422:
        return f"Failed to add Apache License 2.0 to repository **{repo_name}** in {org_name}: 422 Unprocessable Entity. The file might already exist or there are semantic errors. Response: {response.json()}", 'Add License Failed'
    else:
        return f"Failed to add Apache License 2.0 to repository **{repo_name}** in {org_name}: {response.status_code}. Response: {response.text}", 'Add License Failed'

# Function to prompt user for adding a license
def prompt_add_license(repo):
    repo_name = repo['name']
    org_name = repo['owner']['login']
    prompt = f"Do you want to add the Apache License 2.0 to repository {repo_name} in {org_name}? (yes/no): "
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'yes':
            return True
        elif user_input == 'no':
            return False
        else:
            print("Please enter 'yes' or 'no'.")

# Main script
def main():
    try:
        generate_report_only = input("Do you want to generate a report only (yes) or also add licenses (no)? (yes/no): ").strip().lower()
        if generate_report_only not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            return

        generate_report_only = generate_report_only == 'yes'
        
        known_licenses = get_known_licenses()
        logs = []
        csv_data = []

        # Add a comment about how licenses were checked
        logs.append("License Check Report")
        logs.append("="*80)
        logs.append("This report checks each repository in the specified GitHub organizations for the presence of a license file.")
        logs.append("Repositories with a recognized and valid license are noted, while those without a license file or with an unrecognized license are flagged.")
        logs.append("\nDetails:")
        logs.append("1. Fetched the list of repositories for each organization using the GitHub API.")
        logs.append("2. For each repository, fetched the license information using the GitHub API.")
        logs.append("3. Checked if the license key is among the known licenses provided by the GitHub API.")
        logs.append("4. Logged whether each repository has a valid license, an unrecognized license, or no license file.")
        if not generate_report_only:
            logs.append("5. For public repositories without a license file, prompted the user to add an Apache License 2.0.")
        logs.append("\nNote: Generally, all public repositories should have a license to clarify the terms of use, redistribution, and contribution.")
        logs.append("="*80 + "\n")

        logs.append(f"\n{'='*80}")
        logs.append(f"License Check Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logs.append(f"{'='*80}\n")
        
        for org_name in ORG_NAMES:
            logs.append(f"\nOrganization: {org_name}")
            logs.append(f"{'-'*80}")
            repositories = get_org_repositories(org_name)
            for repo in repositories:
                if repo['archived']:
                    log = f"Repository **{repo['name']}** in {org_name} is archived. Skipping..."
                    logs.append(log)
                    logs.append(f"{'-'*80}")
                    csv_data.append([repo['name'], org_name, 'Archived', 'Private' if repo['private'] else 'Public', '', ''])
                    print(log)
                    print(f"{'-'*80}")
                    continue
                
                log, license_status, license_name = check_repo_license(repo, known_licenses)
                logs.append(log)
                logs.append(f"{'-'*80}")
                csv_data.append([repo['name'], org_name, license_status, 'Private' if repo['private'] else 'Public', license_name, log])
                print(log)
                print(f"{'-'*80}")
                if license_status == 'No License':
                    if generate_report_only:
                        logs.append(f"A license is recommended for repository **{repo['name']}** in {org_name}.")
                        logs.append(f"{'-'*80}")
                        csv_data[-1][2] = 'License Recommended'
                        csv_data[-1][4] = 'None'
                        print(f"A license is recommended for repository **{repo['name']}** in {org_name}.")
                        print(f"{'-'*80}")
                    else:
                        if prompt_add_license(repo):
                            exists, content = check_license_file_exists(repo)
                            if exists:
                                logs.append(f"LICENSE file already exists in repository **{repo['name']}** in {org_name}.")
                                logs.append(f"{'-'*80}")
                                csv_data[-1][2] = 'License Exists'
                                csv_data[-1][4] = 'Exists'
                                print(f"LICENSE file already exists in repository **{repo['name']}** in {org_name}.")
                                print(f"{'-'*80}")
                            else:
                                add_log, new_status = add_license(repo, APACHE_LICENSE_CONTENT)
                                logs.append(add_log)
                                logs.append(f"{'-'*80}")
                                csv_data[-1][2] = new_status
                                csv_data[-1][4] = 'Apache License 2.0'
                                csv_data[-1][5] = add_log
                                print(add_log)
                                print(f"{'-'*80}")
                        else:
                            logs.append(f"A license is recommended for repository **{repo['name']}** in {org_name}.")
                            logs.append(f"{'-'*80}")
                            csv_data[-1][2] = 'License Recommended'
                            csv_data[-1][4] = 'None'
                            print(f"A license is recommended for repository **{repo['name']}** in {org_name}.")
                            print(f"{'-'*80}")
            logs.append("\n")
        
        # Save logs to a file
        with open('license_check_logs.txt', 'w') as log_file:
            log_file.write('\n'.join(logs))

        # Save CSV data to a file
        with open('license_check_report.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Repository', 'Organization', 'License Status', 'Private/Public', 'License', 'Notes'])
            writer.writerows(csv_data)
        
        print('\nLogs have been saved to license_check_logs.txt\n')
        print('CSV report has been saved to license_check_report.csv\n')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()