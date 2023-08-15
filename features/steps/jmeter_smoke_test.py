from behave import given, when, then
import os
import subprocess
import json


with open('D:\BehaveProject\data.json') as f:
    data = json.load(f)
    jmeter_path = data['jmeter_path']
    jmx_file = data['jmx_file']
    jtl_file = data['jtl_file']

# Delete the existing jtl file if it exists
if os.path.exists(jtl_file):
    os.remove(jtl_file)


@given('I have JMeter installed')
def check_jmeter_installed(context):
    try:
        # Run JMeter with the -v option to get the version information
        version_output = subprocess.check_output([jmeter_path, '-v'], stderr=subprocess.STDOUT)
        jmeter_version = version_output.decode().strip()
        print(f"JMeter version: {jmeter_version}")
        context.jmeter_installed = True
    except subprocess.CalledProcessError as e:
        print(f"JMeter is not installed or not set up correctly: {e.output.decode()}")
        context.jmeter_installed = False


@when('I run the JMeter test')
def run_jmeter_test(context):
    command = f'{jmeter_path} -n -t {jmx_file} -l {jtl_file} -e -o D:/reports/jmreports'

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        context.jmeter_execution_status = False
        print(f"JMeter execution failed with error: {e}")
    else:
        context.jmeter_execution_status = True


@then('JMeter execution should be successful')
def check_jmeter_execution(context):
    if context.jmeter_execution_status:
        print("JMeter execution completed successfully.")
    else:
        raise AssertionError("JMeter execution failed. Check logs for details.")
