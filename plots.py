import matplotlib.pyplot as plt

if __name__ == "__main__":
    data_size = [8, 16, 32]
    fig, ax = plt.subplots()
    fig.set_size_inches(8, 6)
    times_best_data_dfs = [0.00035663199424743655, 0.00020735001564025878, 0.001297635793685913]
    times_best_data_bfs = [0.00031599783897399904, 0.0005889711380004883, 0.001210303544998169]
    times_best_data_Kahn = [0.00034705305099487304, 0.0005743257999420166, 0.0011499145030975343]
    times_best_data_DFS = [0.00046537065505981444, 0.0008716073036193848, 0.0017542502880096436]
    plt.xlabel("Best Data Size KB")
    plt.ylabel("Time")
    plt.scatter(data_size, times_best_data_dfs, c='k')
    plt.scatter(data_size, times_best_data_bfs, c='g')
    plt.scatter(data_size, times_best_data_Kahn, c='m')
    plt.scatter(data_size, times_best_data_DFS, c='b')
    plt.figtext(0, 0.005, "DFS", fontsize=10, color='k')
    plt.figtext(0.05, 0.005, "BFS", fontsize=10, color='g')
    plt.figtext(0.1, 0.005, "TopSort by Kahn", fontsize=10, color='m')
    plt.figtext(0.28, 0.005, "TopSort on DFS", fontsize=10, color='b')
    plt.show()
    fig2, ax2 = plt.subplots()
    fig2.set_size_inches(8, 6)
    times_worst_data_dfs = [0.000182877779006958, 0.00047372984886169436, 0.0006026360988616944]
    times_worst_data_bfs = [0.0002665855884552002, 0.0004979038238525391, 0.0008137891292572021]
    times_worst_data_Kahn = [0.0003691866397857666, 0.0007694005966186523, 0.001636561393737793]
    times_worst_data_DFS = [0.00016803550720214844, 0.00028990507125854493, 0.0005820722579956054]
    plt.xlabel("Worst Data Size KB")
    plt.ylabel("Time")
    plt.scatter(data_size, times_worst_data_dfs, c='k')
    plt.scatter(data_size, times_worst_data_bfs, c='g')
    plt.scatter(data_size, times_worst_data_Kahn, c='m')
    plt.scatter(data_size, times_worst_data_DFS, c='b')
    plt.figtext(0, 0.005, "DFS", fontsize=10, color='k')
    plt.figtext(0.05, 0.005, "BFS", fontsize=10, color='g')
    plt.figtext(0.1, 0.005, "TopSort by Kahn", fontsize=10, color='m')
    plt.figtext(0.28, 0.005, "TopSort on DFS", fontsize=10, color='b')
    plt.show()
    fig3, ax3 = plt.subplots()
    fig3.set_size_inches(8, 6)
    times_rnd_data_dfs = [0.00018378043174743653, 0.0004103097915649414, 0.0006403689384460449]
    times_rnd_data_bfs = [0.0002825250625610352, 0.0005929431915283203, 0.000742365837097168]
    times_rnd_data_Kahn = [0.00035210800170898436, 0.0009646444320678711, 0.001607431173324585]
    times_rnd_data_DFS = [0.0001625370979309082, 0.0004002871513366699, 0.0006865923404693604]
    plt.xlabel("Random Data Size KB")
    plt.ylabel("Time")
    plt.scatter(data_size, times_rnd_data_dfs, c='k')
    plt.scatter(data_size, times_rnd_data_bfs, c='g')
    plt.scatter(data_size, times_rnd_data_Kahn, c='m')
    plt.scatter(data_size, times_rnd_data_DFS, c='b')
    plt.figtext(0, 0.005, "DFS", fontsize=10, color='k')
    plt.figtext(0.05, 0.005, "BFS", fontsize=10, color='g')
    plt.figtext(0.1, 0.005, "TopSort by Kahn", fontsize=10, color='m')
    plt.figtext(0.28, 0.005, "TopSort on DFS", fontsize=10, color='b')
    plt.show()

