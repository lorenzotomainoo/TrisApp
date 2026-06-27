import random
import pygame

LARGHEZZA, ALTEZZA = 900, 900
DIM_CELL = LARGHEZZA // 3

BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)
VERDE = (0, 255, 0)

giocatore1 = 'X'
giocatore2 = 'O'

def crea_tabellone():
    ret = []
    for _ in range(3):
        t = []
        for _ in range(3):
            t.append(' ')
        ret.append(t)
    return ret

def stampa_tabellone(t, screen):
    spessore = 3

    #! LINEE VERTICALI
    pygame.draw.line(screen, BIANCO, (DIM_CELL, 0), (DIM_CELL, ALTEZZA), spessore)
    pygame.draw.line(screen, BIANCO, (DIM_CELL * 2, 0), (DIM_CELL * 2, ALTEZZA), spessore)

    #! LINEE ORIZZONTALI
    pygame.draw.line(screen, BIANCO, (0, DIM_CELL), (LARGHEZZA, DIM_CELL), spessore)
    pygame.draw.line(screen, BIANCO, (0, DIM_CELL * 2), (LARGHEZZA, DIM_CELL * 2), spessore)

def disegna_mosse(t, screen):
    for riga in range(3):
        for colonna in range(3):
            simbolo = t[riga][colonna]

            if simbolo != ' ':
                x = (colonna * DIM_CELL) + (DIM_CELL // 2)
                y = (riga * DIM_CELL) + (DIM_CELL // 2)

                if simbolo == 'O':
                    raggio = 100
                    spessore_cerchio = 12
                    pygame.draw.circle(screen, VERDE, (x, y), raggio, spessore_cerchio)
                
                elif simbolo == 'X':
                    offset = DIM_CELL // 3
                    spessore_x = 12

                    pygame.draw.line(screen, ROSSO, (x - offset, y - offset), (x + offset, y + offset), spessore_x)
                    pygame.draw.line(screen, ROSSO, (x - offset, y + offset), (x + offset, y - offset), spessore_x)

def controlla_tabellone(t, cella : tuple):
    if t[cella[0]][cella[1]] != ' ':
        return False
    return True

def aggiungi_mossa(t, giocatore, cella: tuple):
    simbolo = giocatore
    t[cella[0]][cella[1]] = simbolo

def controlla_vittoria(t):
    for i in range(3):
        if t[i][0] == t[i][1] == t[i][2] and t[i][0] != ' ': #! RIGHE
            return True
        
        if t[0][i] == t[1][i] == t[2][i] and t[0][i] != ' ': #! COLONNE
            return True
        
    if t[0][0] == t[1][1] == t[2][2] and t[0][0] != ' ': #! DIAGONALE (ALTO SX - BASSO DX)
        return True

    if t[0][2] == t[1][1] == t[2][0] and t[0][2] != ' ': #! DIAGONALE (ALTO DX - BASSO SX)
        return True

    return False

#! ALGORITMO PER FAR GICOARE IL BOT
def controlla_vittoria_simbolo(t, simbolo):
    for i in range(3):
        if t[i][0] == t[i][1] == t[i][2] == simbolo:
            return True
        if t[0][i] == t[1][i] == t[2][i] == simbolo:
            return True
        
    if t[0][0] == t[1][1] == t[2][2] == simbolo: 
        return True
    if t[0][2] == t[1][1] == t[2][0] == simbolo:
        return True
    return False

def mosse_rimanenti(t):
    count = 0
    for riga in range(3):
        for colonna in range(3):
            if t[riga][colonna] == ' ':
                count += 1
    return count

def minimax(t, profondita, is_maximizing):
    if controlla_vittoria_simbolo(t, 'O'):
        return 10 - profondita # Vince il bot
    if controlla_vittoria_simbolo(t, 'X'):
        return profondita - 10 
    if mosse_rimanenti(t) == 0:
        return 0 

    if is_maximizing:
        miglior_punteggio = -float('inf')
        for riga in range(3):
            for colonna in range(3):
                if t[riga][colonna] == ' ':
                    t[riga][colonna] = 'O'
                    punteggio = minimax(t, profondita + 1, False)
                    t[riga][colonna] = ' ' 
                    miglior_punteggio = max(punteggio, miglior_punteggio)
        return miglior_punteggio
    else:
        miglior_punteggio = float('inf')
        for riga in range(3):
            for colonna in range(3):
                if t[riga][colonna] == ' ':
                    t[riga][colonna] = 'X'
                    punteggio = minimax(t, profondita + 1, True)
                    t[riga][colonna] = ' '
                    miglior_punteggio = min(punteggio, miglior_punteggio)
        return miglior_punteggio

def gioca_bot(t, difficolta):
    if difficolta == 1:       
        chance_errore = 0.75  
    elif difficolta == 2:     
        chance_errore = 0.30  
    else:                     
        chance_errore = 0.0   

    if random.random() < chance_errore:
        celle_vuote = []
        for riga in range(3):
            for colonna in range(3):
                if t[riga][colonna] == ' ':
                    celle_vuote.append((riga, colonna))
        return random.choice(celle_vuote)

    miglior_punteggio = -float('inf')
    mossa_migliore = None

    for riga in range(3):
        for colonna in range(3):
            if t[riga][colonna] == ' ':
                t[riga][colonna] = 'O'
                punteggio = minimax(t, 0, False)
                t[riga][colonna] = ' '

                if punteggio > miglior_punteggio:
                    miglior_punteggio = punteggio
                    mossa_migliore = (riga, colonna)
                    
    return mossa_migliore

def main():
    print()
    print("--- BENVENUTO A TRIS ---")
    print("1: Facile (Il bot fa un sacco di errori)")
    print("2: Medio (Il bot è bravino ma si distrae)")
    print("3: Imbattibile (Scordatelo)")
    scelta = input("Scegli la difficoltà (1-2-3): ")
    
    if scelta == '1':
        difficolta = 1
    elif scelta == '2':
        difficolta = 2
    else:
        difficolta = 3 
        
    pygame.init()
    screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
    pygame.display.set_caption("Tris!")
    clock = pygame.time.Clock()

    t = crea_tabellone()
    giocatore_attuale = giocatore1
    numero_mosse = 0
    gioco_finito = False 

    colonna = 0
    riga = 0
    
    while True:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return 

            if event.type == pygame.MOUSEBUTTONDOWN and giocatore_attuale == 'X' and not gioco_finito:
                mouseX, mouseY = event.pos

                colonna = mouseX // DIM_CELL #! indice matrice
                riga = mouseY // DIM_CELL #! indice matrice

                if not controlla_tabellone(t, (riga, colonna)):
                    continue 

                aggiungi_mossa(t, giocatore_attuale, (riga, colonna))
                numero_mosse += 1
                
                if controlla_vittoria(t):
                    print(f'Il giocatore {giocatore_attuale} ha vinto!')
                    gioco_finito = True
                elif numero_mosse == 9:
                    print('Pareggio!')
                    gioco_finito = True
                else:
                    giocatore_attuale = giocatore2

        if giocatore_attuale == 'O' and not gioco_finito:
            mossa_bot = gioca_bot(t, difficolta) 
            
            if mossa_bot is not None:
                riga, colonna = mossa_bot
            
            aggiungi_mossa(t, giocatore_attuale, (riga, colonna))
            numero_mosse += 1

            if controlla_vittoria(t):
                print(f'Il giocatore {giocatore_attuale} ha vinto!')
                gioco_finito = True
            elif numero_mosse == 9:
                print('Pareggio!')
                gioco_finito = True
            else:
                giocatore_attuale = giocatore1

        screen.fill((0, 0, 0))
        
        stampa_tabellone(t, screen)
        disegna_mosse(t, screen)

        pygame.display.flip() 

main()