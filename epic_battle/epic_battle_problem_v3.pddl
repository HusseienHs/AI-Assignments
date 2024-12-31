(define (problem epic-battle1)
  (:domain epicBattle)
  (:objects
    cell1 cell2 cell3 cell4 cell5 cell6 cell7 cell8 cell9 cell10 cell11 cell12 cell13 cell14 cell15 cell16 cell17 cell18 cell19 cell20 cell21 cell22 cell23 cell24 cell25 - cell
    student1 student2 student3 student4 - student
    sword1 - sword
    wand1 - wand
    potionBook1 - potionBook
    fightingTool2- wand
  )
  (:init
   
    (position student1 cell1)   
    (position student2 cell6)  
    (position student3 cell11) 

    (is-warrior student1)
    (is-wizard student2)
    (is-cleric student3)

    (position sword1 cell5)     
    (position wand1 cell20)     
    (position potionBook1 cell15) 

   
    (position swordMaster cell2)  
    (position archWizard cell10) 
    (position potionMaster cell25) 

    ; Position of the dragon
    (position evilDragon cell13)  

  )
  (:goal
    (and
      (vanquished-dragon)
    )
  )
)
