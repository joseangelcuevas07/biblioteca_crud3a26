import flet as ft 

def libro_form():
    titulo_imput = ft.TextField(
        label ="Titulo del libro: ",
        width= 400
    )
    
    autor_imput = ft.TextField(
        label = "Autor del libro: ",
        width= 400
    )
    
    isbn_input = ft.TextField(
        label = "ISBN: ",
        width= 400
    )
    
    mensaje = ft.Text(
        "",
        color = ft.Colors.GREEN
    )
    
    return ft.container(
       padding = 30,
       content = ft.Column(
           controls = [
               ft.Text(
                   "Registrar nuevo libro",
                   size = 24,
                   weight= ft.FontWeight.BOLD
               ),
               
               ft.Text(
                   "Capture los datos básicos del libro",
                   size = 14,
                   color = ft.Colors.BLUE_GREY_600
               ),
               
               titulo_imput,
               autor_imput,
               isbn_input,
               
               ft.ElevatedButton(
                   "Registrar libro",
                   icon = ft.Icon.SAVE 
                   
               )
           ],
           spacing= 15
       )
   )    