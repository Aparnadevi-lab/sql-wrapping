import os

def wrap_statement(statement):
    return (
        'BEGIN\n'
        f'{statement.strip()}\n'
        'EXCEPTION\n'
        '     WHEN OTHERS THEN\n'
        '         RAISE;\n'
        'END;\n/\n'
    )

def process_files(input_dir,output_dir):
    os.makedirs(output_dir,exist_ok=True)
    for filename in os.listdir(input_dir):
        with open(os.path.join(input_dir,filename),'r') as   infile:
            statements = infile.read().strip().split(';')
            wrapped= [wrap_statement(stmt) for stmt in statements if stmt.strip()] 
        with open(os.path.join(output_dir,filename),'w') as outfile:
                 outfile.write('\n'.join(wrapped))

if __name__=='__main__':
    process_files('input_sql','output_sql') 

