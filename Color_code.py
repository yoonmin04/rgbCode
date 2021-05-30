class Color_code:
    es = [' ', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
    es_c = {' ' : (120, 50,0), '~' : (120, 55,5), '!' : (120, 60,10), '@' : (120, 65,15), '#' : (120, 70,20), '$' : (120, 75,25), '%' : (120, 80,30), '^' : (120, 85,35), '&' : (120, 90,40), '*' : (120, 95,45), '(' : (120, 100,50), ')' : (120, 105,55), '-' : (120, 110,60), '_' : (120, 115,65), '+' : (120, 120,70), '=' : (120, 125,75), '{' : (120, 130,80), '}' : (120, 135,85), '[' : (120, 140,90), ']' : (120, 145,95), ':' : (120, 150,100), ';' : (120, 155,105), '"' : (120, 160,110), "'" : (120, 165,115), '<' : (120, 170,120), '>' : (120, 175,125), ',' : (120, 180,130), '.' : (120, 185,135), '?' : (120, 190,140), '/' : (120, 195,145), '\n': (120, 200, 150)}

    keys = ['e', 'i', 'a', 't', 'n', 's', 'o', 'r', 'l', 'd', 'c', 'h', 'u', 'm', 'p', 'f', 'g', 'y', 'w', 'k', 'v', 'b', 'j', 'q', 'x', 'z']
    keys_c = {'e' : (50, 50,0), 'i' : (50, 55,5), 'a' : (50, 60,10), 't' : (50, 65,15), 'n' : (50, 70,20), 's' : (50, 75,25), 'o' : (50, 80,30), 'r' : (50, 85,35), 'l' : (50, 90,40), 'd' : (50, 95,45), 'c' : (50, 100,50), 'h' : (50, 105,55), 'u' : (50, 110,60), 'm' : (50, 115,65), 'p' : (50, 120,70), 'f' : (50, 125,75), 'g' : (50, 130,80), 'y' : (50, 135,85), 'w' : (50, 140,90), 'k' : (50, 145,95), 'v' : (50, 150,100), 'b' : (50, 155,105), 'j' : (50, 160,110), 'q' : (50, 165,115), 'x' : (50, 170,120), 'z' : (50, 175,125), }

    upkeys = ['E', 'I', 'A', 'T', 'N', 'S', 'O', 'R', 'L', 'D', 'C', 'H', 'U', 'M', 'P', 'F', 'G', 'Y', 'W', 'K', 'V', 'B', 'J', 'Q', 'X', 'Z']
    upkeys_c = {'E' : (80, 50,0), 'I' : (80, 55,5), 'A' : (80, 60,10), 'T' : (80, 65,15), 'N' : (80, 70,20), 'S' : (80, 75,25), 'O' : (80, 80,30), 'R' : (80, 85,35), 'L' : (80, 90,40), 'D' : (80, 95,45), 'C' : (80, 100,50), 'H' : (80, 105,55), 'U' : (80, 110,60), 'M' : (80, 115,65), 'P' : (80, 120,70), 'F' : (80, 125,75), 'G' : (80, 130,80), 'Y' : (80, 135,85), 'W' : (80, 140,90), 'K' : (80, 145,95), 'V' : (80, 150,100), 'B' : (80, 155,105), 'J' : (80, 160,110), 'Q' : (80, 165,115), 'X' : (80, 170,120), 'Z' : (80, 175,125), }

    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    nums_c = {'0' : (10, 100, 0), '1' : (10, 110, 10), '2' : (10, 120, 20), '3' : (10, 130, 30), '4' : (10, 140, 40), '5' : (10, 150, 50), '6' : (10, 160, 60), '7' : (10, 170, 70), '8' : (10, 180, 80), '9' : (10, 190, 90)}

    def make_html(material, fn):
        u = "./"+fn+".html"
        file = open(u, "x")
        tag = "<tr>"
        for y in range(len(material)):
            tag += "<td style=\"background-color:rgb"+str(material[y])+"\"></td>"
            #if y%8 == 7:
            #    tag += "</tr><tr>"
        tag += "</tr>"
        template = """
        <!DOCTYPE html>
        <html>
            <head>
                <title></title>
                <meta charset="UTF-8">
                <style>
                    table, td, tr {
                    border : none;
                    border-collapse : collapse;
                }
                td{
                    width: 100px;
                    height: 100px;
                }
                </style>
            </head>
            <body>
                <table>
                    %s
                </table>
            </body>
        </html>
        """%(tag)
        file.write(template)
        file.close()

    def make_code():
        fir = input("Enter What you want\n")
        url = input("Enter file name what you want : ")
        fir_ls = list(fir)
        result = []
        for x in range(len(fir_ls)):
            now  = fir_ls[x]
            if now.isnumeric():
                result.append(Color_code.nums_c[now])
            elif now.isalpha():
                if now.isupper():
                    result.append(Color_code.upkeys_c[now])
                elif now.islower():
                    result.append(Color_code.keys_c[now])
            else:
                result.append(Color_code.es_c[now])
        Color_code.make_html(result, url)
    
    def read_code():
        us = input("Enter PWD : ")
        fil = open(us, 'r')
        l_s = []
        materials = fil.read()
        st = materials.find("<table>")
        en = materials.find("</table>")
        materials = materials[st:en]
        while materials.find("rgb") != -1:
            ist = materials.find("rgb")
            ie = materials.find(")")
            l_s.append(materials[ist+3:ie+1])
            materials = materials[ie+2:en]
        fil.close()
        for z in range(len(l_s)):
            le = l_s[z].find(',')
            iet = (l_s[z][1:le])
            if iet == '10': #숫자
                m = l_s[z]
                a = int(m[-3:-1])
                l_s[z] = str(a//10)
            elif iet == '50': #소문자
                k = list(Color_code.keys_c.keys()) 
                v = list(Color_code.keys_c.values())
                for t in range(len(v)):
                    if str(v[t]) == l_s[z]:
                        l_s[z] = k[t]
                        break               
            elif iet == '80': #대문자
                k = list(Color_code.upkeys_c.keys()) 
                v = list(Color_code.upkeys_c.values())
                for t in range(len(v)):
                    if str(v[t]) == l_s[z]:
                        l_s[z] = k[t]
                        break 
            elif iet == '120': #특수기호
                k = list(Color_code.es_c.keys()) 
                v = list(Color_code.es_c.values())
                for t in range(len(v)):
                    if str(v[t]) == l_s[z]:
                        l_s[z] = k[t]
                        break 
        print("".join(l_s))

    def main():
        print("Hello, I'm RGB color coder")
        print("Now choose one between write mode and read mode", end="")
        intro = input("[W/R]")
        if intro.lower() == "w":
            Color_code.make_code()
        elif intro.lower() == "r":
            Color_code.read_code()
        
Color_code.main()
