charlist = list()
chars = input("str (1/0) - 7 seg distplay: ")
for i in chars:
    try:
        int(i)
        charlist.append(i)
    except:
        print("string not fully of numbers.")
        continue

a = d = g = "---"
f = e = b = c = "|"
print_tamplate = f"""
{f}{a}{a}{a}{a}{a}{a}{a}{a}
{f}                     {b}
{f}                     {b}
{e}{g}{g}{g}{g}{g}{g}{g}{b}  
{e}                     {c}
{e}                     {c}
{d}{d}{d}{d}{d}{d}{d}{d}{c}


"""

print(print_tamplate)
