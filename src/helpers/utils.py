def normalizar_string(string):
    return string.strip().replace('\n', ' ').replace('\t', ' ').strip().replace('  ', ' ').replace('     ', ' ').replace('    ', ' ').replace('   ', ' ').replace('  ', ' ')
