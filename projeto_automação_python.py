import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta") # Coloque aqui a pasta o qual quer organizar

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"],
    "planilhas": [".xlsx", ".xls", ".ods"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
    "documentos_word": [".doc", ".docx", ".odt"],
    "powerpoint": [".pptx", ".ppt"],
    "textos": [".txt", ".rtf", ".md"],
    "videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "audios": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "arquivos_zip": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "executaveis": [".exe", ".bat", ".sh", ".py"],
    "html_css": [".html", ".css", ".js"],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

print("Organização concluída!")
