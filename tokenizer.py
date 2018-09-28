# Lexical process: removing white lines and comments
token = []
user_variables = []
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
reserved_words = ["int", "void", "if", "while", "return", "continue",
                  "break", "scan", "printf", "main", "write", "read", "else"]
symbols = ["(", ")", "{", "}", "[", "]", ",", ";", "+", "-",
           "*", "/", "=", "!", "<", ">", "|", "&"]

assign_compare = ["+", "-", "*", "/", "!", "<", ">", "=", "|", "&"]


def check_token(word):
    # If user variable. include _CSC254
    if (word in symbols or word in reserved_words or word in user_variables
        or word[0] in digits):
        
        # Return Error if letters after digits
        if word[0] in digits:
            for i in range(len(word)):
                if word[i] in digits:
                    continue
                else:
                    raise ValueError('Abort scanning. Invalid token!')
        if word in user_variables:
            word += "_csc254"
        return word
    
    else:

        # Add to dictionary
        user_variables.append(word)
        word += "_csc254"
        return word


def read_line(line):
    char = line[0]
    token_line = []

    # Removing meta statements
    if char != '/' and char != '#' and line != "\n":
        
        # get words
        look_ahead = ""
        quote = False
        for letter in line:

            # Open Quotation
            if letter == '"' and quote == False:
                look_ahead += letter
                quote = True

            # Close Quotation
            elif letter == '"' and quote == True:
                look_ahead += letter
                token_line.append(look_ahead)
                look_ahead = ""
                quote = False;

            # Middle of Quotation
            elif quote == True:
                look_ahead += letter
                
            # Tokens separated by white spaces
            elif letter == ' ':
                if look_ahead != '':
              
                    if (not(look_ahead in reserved_words or look_ahead in user_variables) and
                           len(token_line) == 0):
                        raise ValueError('Abort scanning. Invalid token!')

                    look_ahead = check_token(look_ahead)
                    token_line.append(look_ahead);
                look_ahead = ''

            # Tokens includes symbols
            elif letter in symbols:

                # if token_line == 0 and if letter == -- or ++ otherwise: Throw Error
                
                if look_ahead != '':
                    look_ahead = check_token(look_ahead)
                    token_line.append(look_ahead)
                token_line.append(letter)
                look_ahead = ''   

            else:
                if letter != '\t':
                    look_ahead += letter
            
    elif char == '#':
            token_line = line
            token.append(token_line)

    # Add line of tokens
    if len(token_line) != 0 and char != '#':
        token.append(token_line)

  
# Read each line to process lexical 
def read_file(fo):
    lines = fo.readlines()
    
    for i in range(len(lines)):
        read_line(lines[i])


# Open files to tokenize
def main():
    # Tokenize file
    path = raw_input("enter the filename (ex. tax.c) ")
    fo = open("c_tests/" + path, 'r')
    read_file(fo)
    fo.close()

    # Write result
    fo = open("test_" + path, 'w')
    for i in range(len(token)):
        for j in range(len(token[i])):

            if (j == 0 and token[i][j] == "#"):
                fo.write(token[i])
                break;
            elif (j > 0 and j < len(token[i])-1 and
                token[i][j] in assign_compare and
                (token[i][j] == token[i][j+1] or
                token[i][j+1] == "=" or
                 token[i][j+1][0] in digits)):
                fo.write(token[i][j])
                
            else:
                fo.write(token[i][j] + " ")

    print("Created test_" + path)
    # Close file                    
    fo.close()

main()
