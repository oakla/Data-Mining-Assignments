ncolors = np.size(np.unique(y))
ncolors = np.size(np.unique(y))
    colors = [0]*ncolors
    for color in range(ncolors):
        colors[color] = plt.cm.jet.__call__((color*255)//(ncolors-1))[:3]
    for i, cs in enumerate(np.unique(y)):
        plt.plot(X[(y == cs).ravel(), 0], X[(y == cs).ravel(), 1], 'o',
                 markeredgecolor='k', markerfacecolor=colors[i], markersize=6,
                 zorder=2)
    legend_items = (np.unique(y).tolist())
    for i in range(len(legend_items)):
                legend_items[i] = 'Class: {0}'.format(legend_items[i])
    plt.legend(legend_items, numpoints=1, markerscale=.75, prop={'size': 9})
	
	
	
	N = len(np.unique(y))
    # define the colormap
    cmap = plt.cm.jet
    # extract all colors from the .jet map
    cmaplist = [cmap(i) for i in range(cmap.N)]
    # create the new map
    cmap = cmap.from_list('Custom cmap', cmaplist, cmap.N)
    plt.scatter(X[:,0], X[:,1], c=y.ravel(), cmap=cmap)