import os, re, sys

while True:
    print(
        """El programa debe ser colocado dentro de una carpeta, con el archivo .txt que se desea analizar Si ya cumples con estas condiciones, escribe:s"""
    )
    start = input()
    if start.lower() == "s":
        break
load = "|          |"

dir = os.getcwd().split(os.path.sep)
dir = "\\\\".join(dir)  # estructura de carpetas para Win
dir = dir + "\\\\"
# verificacion de SO
if os.path.exists(dir) == True:
    sis = "W"
else:
    dir = os.getcwd()
    sis = "L_M"

Files = ", ".join(os.listdir())  # genera un str con los elementos
if Files == "":
    while True:
        print(
            "No hay archivos .txt en la carpeta actual, desea analizar otra caperta, introduzca la dirección, si desea salir presione enter"
        )
        p = input()
        if p.lower == "":
            sys.exit()

filter = re.compile(r'([^\s,\.][^\\/:"|*.<>,]+\.txt)')
Files_txt = filter.findall(Files)
print("Archivos .txt encontrados:\n" + "\n".join(Files_txt) + "\n")
Match = []

for txt in Files_txt:
    path = os.path.join(txt)
    task = open(
        path, encoding="UTF-8"
    )  # actualmente no es necesario def el modo r ya que este se activa por def cada vez que llama a open
    emails = task.read()

    Hunter = re.compile(
        r"""(
    [a-zA-Z0-9._%+-]+    @
    (|gmail|hotmail|yahoo|outlook)#[a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )""",
        re.VERBOSE | re.I | re.DOTALL,
    )

    for groups in Hunter.findall(emails):
        Match.append(groups[0])

print("Iniciando")
for i in range(10):
    print("|" + "■" * (i + 1) + load[i + 1 : 10] + "|")


if len(Match) > 0:
    Match = "\n".join(Match)
    txt = os.path.join("Emails_Matched.txt")
    Hunt = open(txt, "w")  # Generacion de archivo txt de elementos conseguidos
    Hunt.write(Match)  # escritura en el txt
    Hunt.close()
    print(
        "\nArchivo: Emails_Matched.txt generado en la carpeta contenedora del programa, para salir presione cualquier tecla"
    )
    s = input()
    if s == "":
        sys.exit()
    else:
        sys.exit()
else:
    print(
        "No se ha encontrado ningun correo en la carpeta contenedora, presione cualquier tecla para salir"
    )
    s = input()
    if s == "":
        sys.exit()
    else:
        sys.exit()
