(define (problem epic-battle-8x8)
  (:domain epicBattle)
  (:objects
  
    cell1 cell2 cell3 cell4 cell5 cell6 cell7 cell8
    cell9 cell10 cell11 cell12 cell13 cell14 cell15 cell16
    cell17 cell18 cell19 cell20 cell21 cell22 cell23 cell24
    cell25 cell26 cell27 cell28 cell29 cell30 cell31 cell32
    cell33 cell34 cell35 cell36 cell37 cell38 cell39 cell40
    cell41 cell42 cell43 cell44 cell45 cell46 cell47 cell48
    cell49 cell50 cell51 cell52 cell53 cell54 cell55 cell56
    cell57 cell58 cell59 cell60 cell61 cell62 cell63 cell64
    - cell

    student1 student2 student3 - student

    sword1 - sword
    wand1 - wand
    potionBook1 - potionBook
  )
  (:init
    
    (position student1 cell1)
    (position student2 cell16)
    (position student3 cell22)

 
    (is-warrior student1)
    (is-wizard student2)
    (is-cleric student3)

   
    (position sword1 cell8)
    (position wand1 cell48)
    (position potionBook1 cell57)

    
    (position swordMaster cell10)
    (position archWizard cell31)
    (position potionMaster cell64)


    (position evilDragon cell63)
  )
  (:goal
    (and
      (vanquished-dragon)
    )
  )
)

