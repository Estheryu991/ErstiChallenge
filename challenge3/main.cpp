#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

int main()
{
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);

    ll v, k; // clone long long
    cin >> v >> k; // short word, nizhen shuai.
    const ll sw = (v - 1) / 3 + 1; // die Name sw ist Befehl.
    const ll sh = (k - 1) / 3 + 1; // const bedeutet die variable kann man nich ändern.
    cout << v * k - sw * sh << '\n'; // wir muss die aussage gegeben. 
 
 
    return EXIT_SUCCESS;

}

