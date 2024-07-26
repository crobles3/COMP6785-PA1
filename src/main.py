# Programming Assignment 1 (PA1) - Alcibiades Bustillo - COMP6785
# Created by: Christian Robles

from structures import Graph
from operations import DFS, ConnectedComponent as CC


def main():
    # Breve Introduction.
    print(
        "\n=========================================================================\n"
        "                            PA1 - COMP6785                               \n"
        "=========================================================================\n"
        "This program allows you to get the topological order, determine if\n"
        "there are cycles, or count the number of connected components for\n"
        "a given graph."
    )

    # Instructions on how to provide the graph.
    print(
        "\nHow to provide the graph: \n"
        "The graph is provided to the program in a .txt file located inside\n"
        "the folder named 'data'. The name must follow the following format:\n"
        "\t<name>DG.txt if it is a directed graph or <name>G.txt\n"
        "\tif is not a directed graph, where <name> can be any\n"
        "\tgroup of characters."
    )

    # Note about how the program determines if the graph is directed or not.
    print(
        "\nNote: a 'D' (uppercase) on the second from right to left\n"
        "position, means that the given graph is directed."
    )

    # Instructions about the file's format.
    print(
        "\nFile Structure: \n"
        "The first line contains a unique integer that indicates the number of\n"
        "nodes. The second line contains another unique integer that indicates\n"
        "the amounts of edges in the graph. The remaining lines contain space\n"
        "separated integer pairs, lets call them u and v, which represents the\n"
        "edge that connects u and v nodes.\n"
    )

    name = ""  # Initialize a variable for the file name.
    while (
        True
    ):  # Iterate until a file name found in the data folder is found, or execution is finished.
        try:  # Tries to open a file based on the given name.
            print(
                "Enter 'exit' to finish execution..."
            )  # Note on how to finish execution.
            name = input(
                "File Name (without .txt): "
            )  # User provide the name of the file.
            file = open(
                "./data/" + name + ".txt", "r"
            )  # Looks and opens the .txt file in the data folder.
            break  # Exit infinite loop.
        except:  # Catches if an error occurs trying to open the file.
            if name == "exit":  # Verifies if the user entered 'exit'.
                return  # Terminates program execution.
            print(
                "\nNo file named {}.txt was found, please try again...\n".format(
                    name
                )
            )

    n = int(next(file))  # Get the first line of the file.
    e = int(next(file))  # Get the second line of the file.

    directed = (
        name[-2] == "D"
    )  # Gets the second character from right to left and determines if is directed.

    G = Graph(
        directed
    )  # Graph G is created.

    print("\nReading the graph...\n")
    for (
        line
    ) in (
        file.readlines()
    ):  # Iterates through the remaining lines of the file (the edges).
        (
            u,
            v,
        ) = (
            line.split()
        )  # Line is divided into two integers, u and v (nodes of the edge).
        G.add_vertex(u)  # Add node u to the graph.
        G.add_vertex(v)  # Add node v to the graph.
        G.add_edge(u, v)  # Add the edge (u,v) to the graph.

    file.close()  # Close the file.

    # Print options to the console.
    print("Choose on of the following options:")
    print("1. Find the topological order of the graph.")
    print("2. Determine if the graph has at least on cycle.")
    print("3. Count the connected components of the graph.\n")

    opt = ""  # Initialize a variable to store the option value.
    while (
        True
    ):  # Iterate until one of the allowed options is provided.
        print(
                "Enter 'exit' to finish execution..."
        )  # Indicates the user how to terminate execution.
        opt = input(
            "Enter the number of the desired option: "
        )  # User enters the desired option.
        if opt == "exit":  # Verifies if the user entered 'exit'.
            return  # Terminates program execution.
        if opt in ["1", "2", "3"]:  # Verifies if the provided option is 1, 2, or 3.
            break  # Exits infinite loop.
        print(
            "\nPlease provide one of the available options.\n"
        )  # Note to the user about the available options.

    print(
        "\nOption {} selected...".format(opt)
    )  # Indicates the chosen option to the user.

    if opt == "1":  # Verifies if option 1 was selected.
        if not directed:  # Verifies if the graph is not directed.
            # Can't determine the topological order of a directed graph.
            print(
                ">> Graph has to be directed in order to determine topological order."
            )
        else:  # Is directed graph.
            cycles, order = DFS(G)  # Applies DFS (Depth First Search) to the graph.
            if cycles:  # Verifies if the graph has cycles
                # Can't have cycles in order to determine topological order.
                print(
                    ">> Graph can't have cycles in order to find the correct topological order."
                )
            else:  # Doesn't have cycles
                arr = order.to_array()  # Array with topological order.
                print(">> Topological Order: ")
                print(
                    ">>", " -> ".join(arr)
                )  # Print topological order with '->' indicating the direction.
    elif opt == "2":  # Verifies if option 2 was selected.
        cycles, _ = DFS(G)  # Applies DFS (Depth First Search) to the graph.
        if cycles:  # Verifies if the graph has cycles.
            # Print cyclic graph message.
            print(">> Graph contains at least one cycle.")
        else:  # No cycles
            # Prints message for acyclic graph.
            print(">> No cycles found in the graph.")
    else:  # If is not option 1 or 2, then it must be option 3.
        count = CC(G)  # Get the number of connected components of the graph.
        # Print the amount of connected components found
        print(">> There where {} connected components found in the graph.".format(count))

    print(
        "\nProgram execution has finished.\n"
    )  # Indicates the user that program execution is over.


if __name__ == "__main__":
    main()
