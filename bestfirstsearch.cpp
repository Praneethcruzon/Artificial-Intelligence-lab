#include<iostream>
#include<vector>
#include<queue>
using namespace std;

class Node {
public:
	string name;
	int huristic;
	vector<Node> adjacent;
	bool visited;
	Node(string n, int h, vector<Node> a) {
		name = n;
		huristic = h;
		adjacent = a;
		visited = false;
	}
	int gethuristic() const{
		return huristic;
	}
};

class Comparator {
public:
	int operator() (const Node &n1, const Node &n2) {
		return n1.gethuristic() > n2.gethuristic();
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
			if(i.visited == false){
				queue.push(i);
				i.visited = true;
			}
		}
	}
	//Node not found
	return path.clear();


}

int main() {
	for(int i=0;i<10;i++){
		Node* 	
	}
	return 0;
}
