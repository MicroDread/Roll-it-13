def make_statement(statment, decoration):
    """"Adds emoji / /additional characters to the start and end of headings"""

    ends = decoration * 3
    print(f" {ends} {statment} {ends}")


# Main routine
make_statement(statment= "I love python" , decoration= "🐍")
make_statement(statment= "Round Results" , decoration= "=")