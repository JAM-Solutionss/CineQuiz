def load_css(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return f'<style>{file.read()}</style>'

