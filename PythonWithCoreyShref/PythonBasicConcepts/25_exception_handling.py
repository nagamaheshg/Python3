try:
    f = open('text2.txt')
   
except FileNotFoundError as e:
    print(e)

except NameError as e:
    print(e)
    
except Exception:
    print(e)
# when try back not through any exception it will come to else block    
else:
    print(f.read())
finally:
    print("Executing finally...")
