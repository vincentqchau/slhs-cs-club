#include <bits/stdc++.h>

using namespace std;

using ll = long long;

using vi = vector<int>;

#define pb push_back
#define rsz resize
#define sz(x) (int)(x).size()
#define lb lower_bound
#define ub upper_bound

using pii = pair<int, int>;

#define f first
#define s second
#define mp make_pair

const ll MOD = 1000000007;

const ll INF = 35566483914425l;

void setIO(string name = "") {
	cin.tie(0)->sync_with_stdio(0);
	if (sz(name)) {
		freopen((name+".in").c_str(), "r", stdin);
		freopen((name+".out").c_str(), "w", stdout);
	}
}

int n, m;

int main() {

    cin >> n >> m;
    vi indegree(n+1);
    vector<vi> adj(n+1);
    for(int i = 0; i < m; i++) {
        int a, b; cin >> a >> b;
        indegree[b]++;
        adj[a].pb(b);
    }
    queue<int> q;
    for(int i = 1; i <= n; i++) {
        if(indegree[i] == 0) {
            q.push(i);
        }
    }
    vi ans;
    while(!q.empty()) {
        int v = q.front(); q.pop();
        ans.pb(v);
        for(int e : adj[v]) {
            if(--indegree[e] == 0) {
                q.push(e);
            }
        }
    }
    if(sz(ans) == n) {
        for(int v : ans) {
            cout << v << " ";
        }
        cout << '\n';
    } else {
        cout << "IMPOSSIBLE" << '\n';
    }

}