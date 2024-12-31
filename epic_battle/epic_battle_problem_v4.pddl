(define (problem epic-battle-6x6)
  (:domain epicBattle)
  (:objects
    
    cell1 cell2 cell3 cell4 cell5 cell6
    cell7 cell8 cell9 cell10 cell11 cell12
    cell13 cell14 cell15 cell16 cell17 cell18
    cell19 cell20 cell21 cell22 cell23 cell24
    cell25 cell26 cell27 cell28 cell29 cell30
    cell31 cell32 cell33 cell34 cell35 cell36
    - cell

    student1 student2 student3 - student


    sword1 - sword
    wand1 - wand
    potionBook1 - potionBook
  )
  (:init
   
    (position student1 cell1)
    (position student2 cell12)
    (position student3 cell18)

    
    (is-warrior student1)
    (is-wizard student2)
    (is-cleric student3)

  
    (position sword1 cell5)
    (position wand1 cell24)
    (position potionBook1 cell30)


    (position swordMaster cell7)
    (position archWizard cell21)
    (position potionMaster cell36)


    (position evilDragon cell34)
  )
  (:goal
    (and
      (vanquished-dragon)
    )
  )
)

