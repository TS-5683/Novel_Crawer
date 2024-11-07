#include "process/LinkList.hpp"

int main() {
    LinkList ll = LinkList({1,2,3,4,5});
    ll.print();
    ll.remove(3);
    ll.print();
    ll.append({1,2,3});
    ll.print();
    return 0;
}