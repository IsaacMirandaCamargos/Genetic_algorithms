# Creating a new selector

def selTournamentWithSharing(individuals, k, tournsize, DISTANCE_LIMIT, SHARING_EXTENT,  fit_attr='fitness'):
  from math import sqrt
  from deap import tools

  # Original fitness scores
  origFitness = [i.fitness.values[0] for i in individuals]

  # Changing the fitness scores based on nearby individuals
  for i in range(len(individuals)):
    sharingSum = 1
    x = individuals[i][0]
    y = individuals[i][1]
    for j in range(len(individuals)):
      if i != j:
        x2 = individuals[j][0]
        y2 = individuals[j][1]
        distance = sqrt((x-x2)**2 + (y-y2)**2)
        if distance < DISTANCE_LIMIT:
          sharingSum += (1-distance/(DISTANCE_LIMIT*SHARING_EXTENT))

    individuals[i].fitness.values = origFitness[i]/sharingSum,


  # Selecting individuals for the next generations
  selected = tools.selTournament(individuals, k, tournsize, fit_attr)


  # Returning the original fitness
  for i, ind in enumerate(individuals):
    ind.fitness.values = origFitness[i],
  
  return selected