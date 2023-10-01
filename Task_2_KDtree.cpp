#include <iostream>
#include <fstream>
#include <vector>
#include <set>

using namespace std;

typedef struct Miner {
    int x, y;
    int cost;
    Miner(int x = 0, int y = 0, int c = 0): x(x), y(y), cost(c) {};
} miner;

typedef struct Kd_Tree_Node {
    int key;
    int dir;
    struct Kd_Tree_Node * left;
    struct Kd_Tree_Node * right;
    Kd_Tree_Node(int key, int dir = 0, struct Kd_Tree_Node * left = NULL, struct Kd_Tree_Node * right = NULL): key(key), dir(dir), left(left), right(right) {};
} kd_tree_node ;

typedef struct Point {
    int x, y;
} point ;

kd_tree_node * kd_tree_construct(kd_tree_node * head, int dir, vector<miner> &vec, int idx) {
    if (head) {
        if (dir == 0) {
            if (vec[head->key].x > vec[idx].x) {
                head->left = kd_tree_construct(head->left, 1 - dir, vec, idx);
            } else {
                head->right = kd_tree_construct(head->right, 1 - dir, vec, idx);
            }
        } else {
            if (vec[head->key].y > vec[idx].y) {
                head->left = kd_tree_construct(head->left, 1 - dir, vec, idx);
            } else {
                head->right = kd_tree_construct(head->right, 1 - dir, vec, idx);
            }
        }
    } else {
        return (new Kd_Tree_Node(idx, dir, NULL, NULL));
    }
    return head;
}

bool point_in_set (miner p, point lu, point rd) {
    return (p.x >= lu.x && p.x <= rd.x && p.y <= lu.y && p.y >= rd.y);
}

set<int> kd_tree_search (kd_tree_node * head, point lu, point rd, vector<miner> &vec) {
    if (head) {
        set<int> ret {};
        if (point_in_set(vec[head->key], lu, rd))
            ret.insert(head->key);
        
        if (head->dir == 0) {
            if (vec[head->key].x > lu.x) {
                set <int> s = kd_tree_search(head->left, lu, rd, vec);
                ret.insert(s.begin(), s.end());
            }
            if (vec[head->key].x <= rd.x) {
                set <int> s = kd_tree_search(head->right, lu, rd, vec);
                ret.insert(s.begin(), s.end());
            }
        } else {
            if (vec[head->key].y > rd.y) {
                set <int> s = kd_tree_search(head->left, lu, rd, vec);
                ret.insert(s.begin(), s.end());
            }
            if (vec[head->key].y <= lu.y) {
                set <int> s = kd_tree_search(head->right, lu, rd, vec);
                ret.insert(s.begin(), s.end());
            }
        }
        return ret;
    } else {
        return set<int> {} ;
    }
}


int main(int argc, const char * argv[]) {
    ofstream cout;
    cout.open ("output.txt");
    ifstream cin;
    cin.open ("input.txt");
    
    
    int n;
    cin >> n;
    vector<miner> vec(n);
    
    kd_tree_node * head = NULL;
    for (int i = 0; i < vec.size(); i++) {
        int x, y, c;
        cin >> x >> y >> c;
        vec[i] = miner(x, y, c);
        head = kd_tree_construct(head, 0, vec, i);
    }
    
    
    
    int m;
    cin >> m;
    for (int i = 0; i < m; i++) {
        int q;
        cin >> q;
        set<int> used {};
        int sum = 0;
        for (int j = 0; j < q; j++) {
            point left_up, right_down;
            cin >> left_up.x >> left_up.y >> right_down.x >> right_down.y;
            set <int> s = kd_tree_search(head, left_up, right_down, vec);
            used.insert(s.begin(), s.end());
        }
        sum = 0;
        for (set<int>::iterator j = used.begin(); j != used.end(); j++) {
            sum += vec[*j].cost;
        }
        cout << sum;
        if (i < m - 1) {
            cout << endl;
        }
    }
    cin.close();
    cout.close();
    return 0;
}
