(define (problem epic-battle1)
  (:domain epicBattle)
  (:objects
    cell1 cell2 cell3 cell4 cell5 cell6 cell7 cell8 cell9 cell10 cell11 cell12 cell13 cell14 cell15 cell16 cell17 cell18 cell19 cell20  - cell
    student1 student2 student3 - student
    sword1 - sword
    wand1 - wand
    potionBook1 - potionBook
  )
  (:init
    (position student1 cell4)
    (position student2 cell5)
    (position student3 cell3)
    (is-warrior student1)
    (is-wizard student2)
    (is-cleric student3)
    (position swordMaster cell8)
    (position archWizard cell9)
    (position potionMaster cell17)
    (position sword1 cell6)
    (position wand1 cell13)
    (position potionBook1 cell12)
    (position evilDragon cell20)
  )
  (:goal
    (and
      (vanquished-dragon)
    )
  )
)
