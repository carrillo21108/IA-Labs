
import algorithms
import timeit
import data

graph = data.getGraph()
weighted_graph = data.getWeightedGraph()
heuristic_graph = data.getHeuristicGraph()
complete_graph = data.getCompleteGraph()


#Resultados
print("Resultado bfs: "+str(algorithms.bfs(graph,'Warm-up activities','Stretching')))
print("Resultado dfs: "+str(algorithms.dfs(graph,'Warm-up activities','Stretching')))
print("Resultado ucs: "+str(algorithms.ucs(weighted_graph,'Warm-up activities','Stretching')))
print("Resultado gbfs: "+str(algorithms.gbfs(heuristic_graph,'Warm-up activities',5,'Stretching')))
print("Resultado astar_s: "+str(algorithms.astar_s(complete_graph,'Warm-up activities',5,'Stretching')))
print("\n")

#Tiempos de ejecucion
#BFS
parametros = (graph,'Warm-up activities','Stretching')
tiempo_transcurrido = timeit.timeit(lambda: algorithms.bfs(*parametros), number=1)
print(f"Tiempo de ejecucion de bfs: {tiempo_transcurrido} segundos")

#DFS
parametros = (graph,'Warm-up activities','Stretching')
tiempo_transcurrido = timeit.timeit(lambda: algorithms.dfs(*parametros), number=1)
print(f"Tiempo de ejecucion de dfs: {tiempo_transcurrido} segundos")

#UCS
parametros = (weighted_graph,'Warm-up activities','Stretching')
tiempo_transcurrido = timeit.timeit(lambda: algorithms.ucs(*parametros), number=1)
print(f"Tiempo de ejecucion de ucs: {tiempo_transcurrido} segundos")

#GBFS
parametros = (heuristic_graph,'Warm-up activities',5,'Stretching')
tiempo_transcurrido = timeit.timeit(lambda: algorithms.gbfs(*parametros), number=1)
print(f"Tiempo de ejecucion de gbfs: {tiempo_transcurrido} segundos")

#ASTAR_S
parametros = (complete_graph,'Warm-up activities',5,'Stretching')
tiempo_transcurrido = timeit.timeit(lambda: algorithms.astar_s(*parametros), number=1)
print(f"Tiempo de ejecucion de astar_s: {tiempo_transcurrido} segundos")