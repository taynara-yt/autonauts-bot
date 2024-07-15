"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot
import pyautogui

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    # bot.browse("http://www.botcity.dev")
    # Implement here your logic...

    bot.execute(r"C:\Users\taysi\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Autonauts.url")
    bot.wait(70000)

    if not bot.find( "btn_start", matching=0.97, waiting_time=50000):
        not_found("btn_start")
    bot.click()
    
    if not bot.find( "carregar_mundo", matching=0.97, waiting_time=50000):
        not_found("carregar_mundo")
    bot.click()
    
    if not bot.find( "escolha_mundo", matching=0.97, waiting_time=50000):
        not_found("escolha_mundo")
    bot.click_relative(-113, 33)

    if not bot.find( "planos_fixados", matching=0.97, waiting_time=50000):
        not_found("planos_fixados")
    bot.click()

       # inicio construção

    if not bot.find( "construir_estrutura", matching=0.97, waiting_time=10000):
        not_found("construir_estrutura")
    bot.click_relative(-782, 526)

    if not bot.find( "bancada", matching=0.97, waiting_time=10000):
        not_found("bancada")
    bot.click_relative(50, 84)
    bot.wait(2000) # Esperar 2 segundos para garantir que o botão foi pressionado e o objeto foi selecionado

    if not bot.find( "posicionar_bancada", matching=0.97, waiting_time=10000):
          not_found("posicionar_bancada")
    bot.click_relative(175, -250)

    if not bot.find( "fechar", matching=0.97, waiting_time=10000):
         not_found("fechar")
    bot.click_relative(953, 533)


    if not bot.find( "pegar_tronco_2", matching=0.97, waiting_time=10000):
        not_found("pegar_tronco_2")
    bot.click_relative(-279, -33)
    bot.wait(2000) # Esperar 2 segundos para garantir que o botão foi pressionado e o objeto foi selecionado

    if not bot.find( "soltar_tronco_1", matching=0.97, waiting_time=10000):
        not_found("soltar_tronco_1")
    bot.right_click_relative(-672, -41)
    bot.wait(7000)  


    if not bot.find( "pegar_tronco_1", matching=0.97, waiting_time=10000):
        not_found("pegar_tronco_1")
    bot.click_relative(-166, -113)
    bot.wait(7000)

    if not bot.find( "soltar_tronco_1", matching=0.97, waiting_time=10000):
        not_found("soltar_tronco_1")
    bot.right_click_relative(-672, -41)
    bot.wait(7000)  # Adicionar tempo de espera para garantir que o tronco seja solto
      

    # pressionar o botão do meio do mouse
    pyautogui.mouseDown(button='middle')
    pyautogui.move(200, -200)
    # soltar o botão do meio do mouse
    pyautogui.mouseUp(button='middle')
    bot.wait(2000)

    # zoom in
    pyautogui.keyDown('ctrl')
    pyautogui.scroll(1000)
    # soltar a tecla Ctrl
    pyautogui.keyUp('ctrl')
    bot.wait(2000)
    
    if not bot.find( "pegar_graveto_1", matching=0.97, waiting_time=10000):
        not_found("pegar_graveto_1")
    bot.click_relative(493, 193)
    bot.wait(2000)
    
    # Voltar a posição e zoom anteriores
    # Reduzir o zoom de volta ao normal
    pyautogui.keyDown('ctrl')
    pyautogui.scroll(-1000)  # Desfazer o zoom com scroll negativo
    pyautogui.keyUp('ctrl')
    bot.wait(2000)
    
    # Pressionar o botão do meio do mouse e mover de volta
    pyautogui.mouseDown(button='middle')
    pyautogui.move(-200, 200)
    pyautogui.mouseUp(button='middle')
    bot.wait(2000)
    
    if not bot.find( "soltar_graveto_1", matching=0.97, waiting_time=10000):
        not_found("soltar_graveto_1")
    bot.right_click_relative(-634, -249)
    bot.wait(4000)
    
    if not bot.find( "pegar_graveto_2", matching=0.97, waiting_time=50000):
        not_found("pegar_graveto_2")
    bot.click_relative(-550, -59)
    bot.wait(3000)

    if not bot.find( "soltar_graveto_1", matching=0.97, waiting_time=10000):
        not_found("soltar_graveto_1")
    bot.right_click_relative(-634, -249)
    bot.wait(5000)

    # mover a tela para a esquerda
    pyautogui.mouseDown(button='middle') #pressionar
    pyautogui.move(500,100)
    pyautogui.mouseUp(button='middle') #soltar
    bot.wait(8000)
    
    # selecionar ferramenta 1 (criação)
    if not bot.find( "ferramenta", matching=0.97, waiting_time=10000):
        not_found("ferramenta")
    bot.click_relative(-128, 10)
    bot.wait(2000)
    
    if not bot.find( "machado_1", matching=0.97, waiting_time=10000):
        not_found("machado_1")
    bot.click()
    bot.wait(2000)

     #pegar vareta
    
    if not bot.find( "pegar_vareta_1", matching=0.97, waiting_time=10000):
        not_found("pegar_vareta_1")
    bot.click_relative(-665, -63)
    bot.wait(8000)
    
    # reutilizando pra soltar a vareta
    if not bot.find( "soltar_pedra", matching=0.97, waiting_time=10000):
        not_found("soltar_pedra")
    bot.right_click_relative(-117, 89)
    bot.wait(8000)
    
    #pegar pedra
    if not bot.find( "pedra_1", matching=0.97, waiting_time=10000):
        not_found("pedra_1")
    bot.click_relative(-731, -114)
    bot.wait(8000)

    # reutilizando pra soltar a vareta
    if not bot.find( "soltar_pedra", matching=0.97, waiting_time=10000):
        not_found("soltar_pedra")
    bot.right_click_relative(-117, 89)
    bot.wait(9000)

    # selecionar ferramenta 2 (criação) pá
    if not bot.find( "ferramenta", matching=0.97, waiting_time=50000):
        not_found("ferramenta")
    bot.click_relative(-128, 10)
    bot.wait(4000)

    if not bot.find( "selecionar_pa", matching=0.97, waiting_time=10000):
        not_found("selecionar_pa")
    bot.click()
    bot.wait(2000)
    
    if not bot.find( "pegar_pedra_2", matching=0.97, waiting_time=10000):
        not_found("pegar_pedra_2")
    bot.click_relative(111, 196)
    bot.wait(8000)
    
    # reutilizando - soltar a pedra 2
    if not bot.find( "soltar_pedra", matching=0.97, waiting_time=10000):
        not_found("soltar_pedra")
    bot.right_click_relative(-117, 89)
    bot.wait(9000)
    
    if not bot.find( "pegar_vareta_2", matching=0.97, waiting_time=10000):
        not_found("pegar_vareta_2")
    bot.click_relative(180, 231)
    bot.wait(8000)
    
     # reutilizando - soltar a vareta_2
    if not bot.find( "soltar_pedra", matching=0.97, waiting_time=10000):
        not_found("soltar_pedra")
    bot.right_click_relative(-117, 89)
    bot.wait(9000)

     # selecionar ferramenta 3
    if not bot.find( "ferramenta", matching=0.97, waiting_time=50000):
        not_found("ferramenta")
    bot.click_relative(-128, 10)
    bot.wait(4000)
    
    if not bot.find( "selecionar_machado", matching=0.97, waiting_time=10000):
        not_found("selecionar_machado")
    bot.click()
    bot.wait(4000) 
      
    if not bot.find( "pegar_vareta_3", matching=0.97, waiting_time=10000):
          not_found("pegar_vareta_3")
    bot.click_relative(-660, 186)
    bot.wait(4000)
    
    if not bot.find( "soltar_vareta_3", matching=0.97, waiting_time=10000):
        not_found("soltar_vareta_3")
    bot.right_click_relative(-109, 180)
    bot.wait(9000)
    
    if not bot.find( "pegar_pedra_3", matching=0.97, waiting_time=10000):
        not_found("pegar_pedra_3")
    bot.click_relative(-779, 188)
    bot.wait(4000)
    
    if not bot.find( "soltar_vareta_3", matching=0.97, waiting_time=10000):
        not_found("soltar_vareta_3")
    bot.right_click_relative(-109, 180)
    bot.wait(9000)
    
    if not bot.find( "mao_machado", matching=0.97, waiting_time=10000):
        not_found("mao_machado")
    bot.click_relative(-121, 88)
    
    if not bot.find( "cortar_arvore_1", matching=0.97, waiting_time=10000):
        not_found("cortar_arvore_1")
    bot.click_relative(-511, 180)
    
    if not bot.find( "cortar_arvore_2", matching=0.97, waiting_time=10000):
        not_found("cortar_arvore_2")
    bot.click_relative(-341, -121)
    bot.wait(4000)
    
    if not bot.find( "cortar_arvore_3", matching=0.97, waiting_time=10000):
        not_found("cortar_arvore_3")
    bot.click_relative(-371, 166)
    bot.wait(4000)
    
    if not bot.find( "guardar_ferramenta_machado", matching=0.97, waiting_time=10000):
        not_found("guardar_ferramenta_machado")
    bot.click()

    # cavar buraco
    if not bot.find( "colocar_pa_mao", matching=0.97, waiting_time=10000):
        not_found("colocar_pa_mao")
    bot.click_relative(-69, -307)
    bot.wait(4000)
    
    if not bot.find( "cavar_buraco_1", matching=0.97, waiting_time=10000):
        not_found("cavar_buraco_1")
    bot.click_relative(-619, 316)
    bot.wait(4000)
    
    if not bot.find( "cavar_buraco_2", matching=0.97, waiting_time=10000):
        not_found("cavar_buraco_2")
    bot.click_relative(-553, -31)
    bot.wait(4000)
    
    if not bot.find( "cavar_buraco_3", matching=0.97, waiting_time=10000):
        not_found("cavar_buraco_3")
    bot.click_relative(-524, -35)
    bot.wait(4000)
    
    if not bot.find( "soltar_ferramenta", matching=0.97, waiting_time=10000):
        not_found("soltar_ferramenta")
    bot.right_click_relative(-527, -68)
    
    # plantar semente 1
    if not bot.find( "pegar_semente_1", matching=0.97, waiting_time=10000):
        not_found("pegar_semente_1")
    bot.click_relative(-547, -4)
    
    if not bot.find( "plantar_semente_1", matching=0.97, waiting_time=10000):
        not_found("plantar_semente_1")
    bot.right_click_relative(-542, 413)

    # estrutura roboles
    if not bot.find( "construir_estrutura", matching=0.97, waiting_time=10000):
        not_found("construir_estrutura")
    bot.click_relative(-782, 526)

    if not bot.find( "estrutura_robo", matching=0.97, waiting_time=10000):
        not_found("estrutura_robo")
    bot.click_relative(-704, 48)
    
    if not bot.find( "colocar_estrutura_robo", matching=0.97, waiting_time=10000):
        not_found("colocar_estrutura_robo")
    bot.click_relative(-324, -250)
    
    if not bot.find( "fechar", matching=0.97, waiting_time=10000):
         not_found("fechar")
    bot.click_relative(953, 533)
    
    if not bot.find( "tronco_estrutura_robo", matching=0.97, waiting_time=10000):
        not_found("tronco_estrutura_robo")
    bot.click_relative(-626, 300)
    bot.wait(3000)
    
    if not bot.find( "posicionar_estrutura_robo", matching=0.97, waiting_time=10000):
        not_found("posicionar_estrutura_robo")
    bot.right_click_relative(-391, 186)
    bot.wait(3000)

    # mover a tela para a esquerda
    pyautogui.mouseDown(button='middle') #pressionar
    pyautogui.move(400,-160)
    pyautogui.mouseUp(button='middle') #soltar
    bot.wait(2000)

    if not bot.find( "abrir_espaco", matching=0.97, waiting_time=10000):
        not_found("abrir_espaco")
    bot.click_relative(-462, 92)
    bot.wait(4000)

     # mover a tela para a direita
    pyautogui.mouseDown(button='middle') #pressionar
    pyautogui.move(-450,-50)
    pyautogui.mouseUp(button='middle') #soltar
    bot.wait(2000)
  
    if not bot.find( "arvore_robo_1", matching=0.97, waiting_time=10000):
        not_found("arvore_robo_1")
    bot.click_relative(-694, 166)
    bot.wait(2000)
    
    if not bot.find( "soltar_arvore_robo_2", matching=0.97, waiting_time=10000):
        not_found("soltar_arvore_robo_2")
    bot.right_click_relative(-188, -326)
    bot.wait(10000)

    # pegar machado
    if not bot.find( "pegar_machado", matching=0.97, waiting_time=10000):
        not_found("pegar_machado")
    bot.click()
    
    if not bot.find( "tabua_1", matching=0.97, waiting_time=10000):
        not_found("tabua_1")
    bot.click_relative(-693, -288)
    
    if not bot.find( "tabua_2", matching=0.97, waiting_time=10000):
        not_found("tabua_2")
    bot.click_relative(-598, -264)
    bot.wait(4000)
    
    #deixar machado
    if not bot.find( "soltar_machado", matching=0.97, waiting_time=10000):
         not_found("soltar_machado")
    bot.right_click_relative(-613, -213)
      
    if not bot.find( "pegar_tabua_1", matching=0.97, waiting_time=10000):
        not_found("pegar_tabua_1")
    bot.click_relative(-739, 18)
    bot.wait(2000)

    #reutilizar para tabua
    if not bot.find( "soltar_arvore_robo_2", matching=0.97, waiting_time=10000):
        not_found("soltar_arvore_robo_2")
    bot.right_click_relative(-188, -326)
    bot.wait(8000)
    
    if not bot.find( "pegar_tabua_2", matching=0.97, waiting_time=10000):
        not_found("pegar_tabua_2")
    bot.click_relative(-671, -212)
    bot.wait(6000)

     #reutilizar para tabua
    if not bot.find( "soltar_arvore_robo_2", matching=0.97, waiting_time=10000):
        not_found("soltar_arvore_robo_2")
    bot.right_click_relative(-188, -326)
    bot.wait(8000)
    
    if not bot.find( "pegar_tabua_3", matching=0.97, waiting_time=10000):
        not_found("pegar_tabua_3")
    bot.click_relative(-688, -236)
    bot.wait(6000)
    
    #reutilizar para tabua
    if not bot.find( "soltar_arvore_robo_2", matching=0.97, waiting_time=10000):
        not_found("soltar_arvore_robo_2")
    bot.right_click_relative(-188, -326)
    bot.wait(8000)
    
    if not bot.find( "pegar_semente_2", matching=0.97, waiting_time=10000):
        not_found("pegar_semente_2")
    bot.click_relative(-705, -293)
    bot.wait(7000)
    
    if not bot.find( "plantar_semente_2", matching=0.97, waiting_time=10000):
        not_found("plantar_semente_2")
    bot.right_click_relative(-296, 77)
    bot.wait(8000)
    
    if not bot.find( "pegar_semente_3", matching=0.97, waiting_time=10000):
        not_found("pegar_semente_3")
    bot.click_relative(-592, 133)
    bot.wait(7000)
    
    if not bot.find( "plantar_semente_3", matching=0.97, waiting_time=10000):
        not_found("plantar_semente_3")
    bot.right_click_relative(-265, -15)
    bot.wait(6000)
    
    #plano completo 1
    if not bot.find( "plano_completo_1", matching=0.97, waiting_time=10000):
         not_found("plano_completo_1")
    bot.click()
    bot.wait(2000)
     
    if not bot.find( "chapeu_lenhador", matching=0.97, waiting_time=10000):
        not_found("chapeu_lenhador")
    bot.click()
    bot.wait(2000)
    
    if not bot.find( "bloco_lenhador", matching=0.97, waiting_time=10000):
        not_found("bloco_lenhador")
    bot.click_relative(367, 140)
    bot.wait(2000)
    
    if not bot.find( "silvicultura", matching=0.97, waiting_time=10000):
        not_found("silvicultura")
    bot.click_relative(604, 62)
    bot.wait(2000)
    
    if not bot.find( "pegar_tronco_3", matching=0.97, waiting_time=10000):
        not_found("pegar_tronco_3")
    bot.click_relative(-610, -14)
    bot.wait(8000)
    

    if not bot.find( "soltar_tronco_3", matching=0.97, waiting_time=10000):
        not_found("soltar_tronco_3")
    bot.right_click_relative(-339, -76)
    bot.wait(8000)
    
    if not bot.find( "pegar_tronco_4", matching=0.97, waiting_time=10000):
        not_found("pegar_tronco_4")
    bot.click_relative(-911, -146)
    bot.wait(8000)

    #reutilizando 
    if not bot.find( "soltar_tronco_3", matching=0.97, waiting_time=10000):
        not_found("soltar_tronco_3")
    bot.right_click_relative(-339, -76)
    bot.wait(8000)
    
    if not bot.find( "pegar_vareta_4", matching=0.97, waiting_time=10000):
        not_found("pegar_vareta_4")
    bot.click_relative(-715, -322)
    bot.wait(8000)
    
     #reutilizando 
    if not bot.find( "soltar_tronco_3", matching=0.97, waiting_time=10000):
        not_found("soltar_tronco_3")
    bot.right_click_relative(-339, -76)
    bot.wait(9000)
    
    if not bot.find( "pegar_vareta_5", matching=0.97, waiting_time=10000):
        not_found("pegar_vareta_5")
    bot.click_relative(-358, -212)
    bot.wait(5000)
    
     #reutilizando 
    if not bot.find( "soltar_tronco_3", matching=0.97, waiting_time=10000):
        not_found("soltar_tronco_3")
    bot.right_click_relative(-339, -76)
    bot.wait(5000)
    
    #mudar perspectiva
    pyautogui.mouseDown(button='middle') 
    pyautogui.move(0, 200)  
    pyautogui.mouseUp(button='middle')  
    bot.wait(3000)
    
    # finalizar ferramentas! (machado 2)
    if not bot.find( "selecionar_ferramentas_2", matching=0.97, waiting_time=10000):
          not_found("selecionar_ferramentas_2")
    bot.click_relative(-362, -158)
    bot.wait(3000)

    if not bot.find( "machado_1", matching=0.97, waiting_time=10000):
        not_found("machado_1")
    bot.click()
    bot.wait(2000)

     #pegar vareta
    if not bot.find( "pegar_vareta_8", matching=0.97, waiting_time=10000):
        not_found("pegar_vareta_8")
    bot.click_relative(195, 338)
    bot.wait(5000)

     #reutilizar para clicar novamente na bancada
    if not bot.find( "soltar_vareta_6", matching=0.97, waiting_time=10000):
        not_found("soltar_vareta_6")
    bot.right_click_relative(-361, -47)
    bot.wait(5000)


     #pegar pedra
    if not bot.find( "pegar_pedra_4", matching=0.97, waiting_time=10000):
        not_found("pegar_pedra_4")
    bot.click_relative(-628, -305)
    bot.wait(6000)
    
    if not bot.find( "soltar_vareta_6", matching=0.97, waiting_time=10000):
        not_found("soltar_vareta_6")
    bot.right_click_relative(-361, -47)
    bot.wait(7000)
    #finalizou machado 2
    
    #inicio machado 3
    #pegar vareta 
    if not bot.find( "pegar_vareta_9", matching=0.97, waiting_time=10000):
        not_found("pegar_vareta_9")
    bot.click_relative(89, 483)
    bot.wait(8000)

    if not bot.find( "soltar_vareta_6", matching=0.97, waiting_time=10000):
        not_found("soltar_vareta_6")
    bot.right_click_relative(-361, -47)
    bot.wait(6000)

    #pegar pedra
    if not bot.find( "pegar_pedra_5", matching=0.97, waiting_time=10000):
        not_found("pegar_pedra_5")
    bot.click_relative(-572, -17)
    bot.wait(5000)
    
    #reutilizar para clicar novamente na bancada
    if not bot.find( "soltar_vareta_6", matching=0.97, waiting_time=10000):
        not_found("soltar_vareta_6")
    bot.right_click_relative(-361, -47)
    bot.wait(5000)
    #finalizou machado 3


    
     # finalizar ferramentas! (pa 2)
    if not bot.find( "selecionar_pa_2", matching=0.97, waiting_time=10000):
           not_found("selecionar_pa_2")
    bot.click_relative(-292, -136)
    bot.wait(2000)
    
    if not bot.find( "selecionar_pa", matching=0.97, waiting_time=10000):
        not_found("selecionar_pa")
    bot.click()
    bot.wait(2000)

    #pegar pedra
    if not bot.find( "pegar_pedra_6", matching=0.97, waiting_time=10000):
        not_found("pegar_pedra_6")
    bot.click_relative(-606, 116)
    bot.wait(5000)
    
    #reutilizar para clicar novamente na bancada
    if not bot.find( "soltar_vareta_6", matching=0.97, waiting_time=10000):
        not_found("soltar_vareta_6")
    bot.right_click_relative(-361, -47)
    bot.wait(5000)

    #pegar vareta
    if not bot.find( "pegar_vareta_10", matching=0.97, waiting_time=10000):
        not_found("pegar_vareta_10")
    bot.click_relative(416, 244)
    bot.wait(5000)
    
    #reutilizar para clicar novamente na bancada
    if not bot.find( "soltar_vareta_6", matching=0.97, waiting_time=10000):
        not_found("soltar_vareta_6")
    bot.right_click_relative(-361, -47)
    bot.wait(5000)
    #finalizou pa 2
    
    #inicio pa 3
    if not bot.find( "pegar_vareta_11", matching=0.97, waiting_time=10000):
         not_found("pegar_vareta_11")
    bot.click_relative(-417, -245)
    bot.wait(5000)
    
    #reutilizar para clicar novamente na bancada
    if not bot.find( "soltar_vareta_6", matching=0.97, waiting_time=10000):
        not_found("soltar_vareta_6")
    bot.right_click_relative(-361, -47)
    bot.wait(5000)
    
    #pegar pedra
    if not bot.find( "pegar_pedra_7", matching=0.97, waiting_time=10000):
         not_found("pegar_pedra_7")
    bot.click_relative(-519, -344)
    bot.wait(5000)
     
     #reutilizar para clicar novamente na bancada
    if not bot.find( "soltar_vareta_6", matching=0.97, waiting_time=10000):
        not_found("soltar_vareta_6")
    bot.right_click_relative(-361, -47)
    bot.wait(7000)
    #finalizou pa 3

    #iniciar picareta 2
    if not bot.find( "selecionar_ferramenta_3", matching=0.97, waiting_time=10000):
         not_found("selecionar_ferramenta_3")
    bot.click_relative(-300, -115)
    bot.wait(2000) 
    
    if not bot.find( "selecionar_picareta_ult", matching=0.97, waiting_time=10000):
        not_found("selecionar_picareta_ult")
    bot.click()
    bot.wait(2000)

    #pegar pedra 2
    if not bot.find( "pegar_pedra_8", matching=0.97, waiting_time=10000):
         not_found("pegar_pedra_8")
    bot.click_relative(-592, -254)
    bot.wait(8000)
     
      #reutilizar para clicar novamente na bancada
    if not bot.find( "soltar_vareta_6", matching=0.97, waiting_time=10000):
        not_found("soltar_vareta_6")
    bot.right_click_relative(-361, -47)
    bot.wait(7000)

    #pegar vareta
    if not bot.find( "pegar_vareta_12", matching=0.97, waiting_time=10000):
        not_found("pegar_vareta_12")
    bot.click_relative(-614, -292)
    bot.wait(8000)
    
     #reutilizar para clicar novamente na bancada
    if not bot.find( "soltar_vareta_6", matching=0.97, waiting_time=10000):
        not_found("soltar_vareta_6")
    bot.right_click_relative(-361, -47)
    bot.wait(7000)
    #finalizou picareta 2
     
     #pegar pedra 
    if not bot.find( "pegar_pedra_9", matching=0.97, waiting_time=10000):
          not_found("pegar_pedra_9")
    bot.click_relative(-590, -359)
    bot.wait(8000)
      
      #reutilizar para clicar novamente na bancada
    if not bot.find( "soltar_vareta_6", matching=0.97, waiting_time=10000):
        not_found("soltar_vareta_6")
    bot.right_click_relative(-361, -47)
    bot.wait(7000)

    #pegar vareta
    if not bot.find( "pegar_vareta_13", matching=0.97, waiting_time=10000):
         not_found("pegar_vareta_13")
    bot.click_relative(-676, -276)
    bot.wait(8000)
     
     #reutilizar para clicar novamente na bancada
    if not bot.find( "soltar_vareta_6", matching=0.97, waiting_time=10000):
        not_found("soltar_vareta_6")
    bot.right_click_relative(-361, -47)
    bot.wait(7000)
    #finalizou picareta 3
     
     #plano completo - ferramentas
    if not bot.find( "plano_completo_ferramentas", matching=0.97, waiting_time=10000):
          not_found("plano_completo_ferramentas")
    bot.click_relative(131, 310)
    bot.wait(2000)
    
    if not bot.find( "plano_ok_1", matching=0.97, waiting_time=10000):
        not_found("plano_ok_1")
    bot.click_relative(141, 194)
    bot.wait(2000)
    
    if not bot.find( "plano_ok_2", matching=0.97, waiting_time=10000):
        not_found("plano_ok_2")
    bot.click_relative(229, 193)
    bot.wait(2000)
    
    if not bot.find( "plano_ok_3", matching=0.97, waiting_time=10000):
        not_found("plano_ok_3")
    bot.click_relative(509, 63)
    bot.wait(2000)
    # finalização do plano ferramentas
      
      
    #pausar
    if not bot.find( "pausar", matching=0.97, waiting_time=10000):
         not_found("pausar")
    bot.click()
    bot.wait(2000)
    
    #sair
    if not bot.find( "sair", matching=0.97, waiting_time=10000):
         not_found("sair")
    bot.click()
    bot.wait(2000)
     
    if not bot.find( "sair_mundo", matching=0.97, waiting_time=10000):
        not_found("sair_mundo")
    bot.click()
    bot.wait(2000)
    
    #finalizar
    if not bot.find( "final_bot", matching=0.97, waiting_time=10000):
         not_found("final_bot")
    bot.click_relative(124, 34)
    bot.wait(2000)
     
    if not bot.find( "sair_autonauts", matching=0.97, waiting_time=10000):
         not_found("sair_autonauts")
    bot.click_relative(79, 122)
    bot.wait(2000)
        

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()




























