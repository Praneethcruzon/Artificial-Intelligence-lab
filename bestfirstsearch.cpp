#include<iostream>
#include<vector>
#include<queue>
using namespace std;

class Node {
public:
	string name;
	int dist;
	vector<Node> adjacent;
	bool visited;
	Node(string n, int d, vector<Node> a) {
		name = n;
		dist = d;
		adjacent = a;
		visited = false;
	}
	int getdist() const{
		return dist;
	}
};

class Comparator {
public:
	int operator() (const Node &n1, const Node &n2) {
		return n1.getdist() > n2.getdist();
	}
};

vector<Node> bestfirstsearch(Node &start, Node &destination) {
	priority_queue<Node, vector<Node>, Comparator> queue;
	queue.push(start);
	vector<Node> path;
	while (queue.empty() == false) {
		Node n = queue.top();
		if (n.name == destination.name) {
			path.push_back(n);
			return path;
		}
		queue.pop();
		path.push_back(n);
		for (Node i : n.adjacent) {
			queue.push(i);
		}
	}


}

int main() {

	return 0;
}