#include <iostream>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
using namespace std;


// Adjacency list: build nodes, storing weight and identification #
struct Node
{
    double weight;
    int num; 
};

// Prim's MST
struct MST_data
{
    double tree_weight;
    bool isMST;
};

// Calc. xclusion dist. b/ween variables
double distance(vector<double> v1, vector<double> v2)
{
    double sum = 0.0;
    for (size_t i = 0; i < v1.size(); i++)
    {
        double diff = v1[i] - v2[i];
        sum += pow(diff,2); // square
    }
    return sqrt(sum);
}

// Pruning strategy implementation
vector<vector<double> > generateGraph(int numpoints, int dimension)
{
    srand((unsigned)time(NULL)); 
    if (dimension == 0) // alter 0 dimension 
    {
        dimension = 1;
    }
    vector<vector<double> > v(numpoints, vector<double>(dimension)); // store coords for e/ node as 2d vector 
    for (int i = 0; i < numpoints; i++)
    {
        for (int j = 0; j < dimension; j++)
        {
            v[i][j] = static_cast<double>(rand()) / RAND_MAX; 
        }
    } 

    return v;
}

// Adjacency list (pruning)
// The baseline is the (length (MST) to previous (MST) (half vertices))^-1 + 20% from 2^7. From lecture and trials to prevent overpruning and runtime complexity. 
vector<vector<Node> > adjacencyList(vector<vector<double> > graph)
{
    vector<vector<Node> > list;
    int num_points = graph.size();

    for (int i = 0; i < num_points; i++)
    {
        vector<Node> m;

        for (int j = 0; j < num_points; j++)
        {
            if (i == j)
                continue; // no edge between 
            double baseline;

            Node n;
            n.num = j;
            if (graph[i].size() == 1)
            {
                n.weight = (double)rand() / RAND_MAX;  // weight = random number 0 to 1 
            }
            else
            {
                n.weight = distance(graph[i], graph[j]); // weight = euclidean distance between the two points
            }

            // Determine pruning value 
            if (graph[i].size() == 1)
            {
                baseline = 1.25;
            }
            else if (graph[i].size() == 2)
            {
                baseline = (double)1 * pow((0.9595098106), log2(num_points) - 7);
            }
            else if (graph[i].size() == 3)
            {
                baseline = (double)1 * pow((0.88160055741), log2(num_points) - 7);
            }
            else if (graph[i].size() == 4)
            {
                baseline = (double)1 * pow((0.850122782), log2(num_points) - 7);
            }
            //Prune IFF weight(edge) > baseline
            if (n.weight >= baseline)
                continue; 

            m.push_back(n);
        }
        list.push_back(m); // push back [k,h] w/ node structure 
    }

    return list;
}

// Heap operations
void heapify(vector<Node> &heap, int i)
{
    int minimum = i;
    int left_par = i * 2 + 1;
    int right_par = i * 2 + 2;

    // If parents are available, move
    if (left_par < heap.size() &&  heap[left_par].weight < heap[minimum].weight)
    {
        minimum = left_par;
    }

    if (right_par < heap.size() && heap[right_par].weight < heap[minimum].weight)
    {
        minimum = right_par;
    }

    // Swap Heap
    if (minimum != i)
    {
        swap(heap[i], heap[minimum]);
        heapify(heap, minimum);
    }
};

// Via Lecture
void insertHeap(vector<Node> &heap, int node, double weight)
{
    Node v = {weight, node};
    heap.push_back(v);
    if (heap.size() > 1)
    {
        const int mid = (heap.size() / 2) - 1;
        for (int i = mid; i >= 0; i--)
        {
            heapify(heap, i);
        }
    }
};

struct Node extractMin(vector<Node> &heap)
{
    swap(heap.front(), heap.back());
    double min_weight = heap.back().weight;
    int min_vertex = heap.back().num;
    heap.pop_back();
    heapify(heap, 0);
    Node min_node = {min_weight, min_vertex};
    return min_node;
};


struct MST_data primsMST(int num_vertices, vector<vector<Node> > graph)
{
    double treeWeight = 0.0;
    bool isMST = true;
    vector<Node> heap;
    Node m;
    bool in_MST[graph.size()]; // keeps track of tree
    memset(in_MST, false, sizeof(bool) * graph.size());
    m.weight = 0;
    m.num = 0;
    heap.push_back(m);

    // from lecture
    while (!heap.empty())
    {
        Node m;
        m = extractMin(heap);
        if (in_MST[m.num])
        {
            continue;
        }

        in_MST[m.num] = true; // keep track of tree
        treeWeight += m.weight;
        for (int i = 0; i < graph[m.num].size(); i++)
        {
            int neighbor = graph[m.num][i].num;
            if (in_MST[neighbor])
            {
                continue;
            }
            insertHeap(heap, neighbor, graph[m.num][i].weight);
        }
    };

    // MST is complete
    for (int i = 0; i < graph.size(); i++)
    {
        if (!in_MST[i]) // not false 
        {
            isMST = false;
            break;
        }
    }
    MST_data prims = {.tree_weight = treeWeight, .isMST = isMST};
    return prims;
};

int main(int argc, char *argv[])
{
    if (argc != 5)
    {
        printf("Wrong number of arguments\n");
        abort();
    } 
    // Via handout: flag, numpoints, numtrials, and dimension from CMDline
    int flag = atoi(argv[1]);
    int numpoints = atoi(argv[2]);
    int numtrials = atoi(argv[3]);
    int dimension = atoi(argv[4]);

    double average;

    // e/ trial gets adjacency list from graph 
    for (int i = 0; i < numtrials; i++)
    {
        vector<vector<Node> > k = adjacencyList(generateGraph(numpoints, dimension));
        MST_data ans = primsMST(numpoints, k); // run prims
        average += ans.tree_weight/numtrials; // add avg weight
        assert(ans.isMST); // ensure its a MST
    }

    cout << "number of points: " << numpoints << " "
         << "dimensions: " << dimension << "\naverage weight: " << average << "\n";

    return 0;
}