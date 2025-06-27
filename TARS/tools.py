import subprocess


def get_special_message():
    return "This is a special message from TARS! 123456"


def call_node_script():
    try:
        result = subprocess.run(['node', 'TARS/node_script.js'], capture_output=True, text=True, check=True)
        return {'status': 'success', 'output': result.stdout.strip()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error_message': str(e)} 