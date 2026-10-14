letter = '''Dear <|Name|>,
                  Congratulations!
                  You are selected!
                  <|Date|>'''
                  
print(letter.replace("<|Name|>", "Tripti@Sharma").replace("<|Date|>", "~09/06/2026"))