#include <iostream>
#include <vector>
using namespace std;

class ListNode {
public:
    int val;
    ListNode *next;

    ListNode(int value, ListNode *node = nullptr) {
        val = value;
        next = node;
    }

    ListNode(ListNode *ln) {
        val = ln->val;
        ListNode *node = this;
        while (ln->next) {
            node->next = new ListNode(ln->next);
            ln = ln->next;
            node = node->next;
        }
    }

    ListNode(const vector<int> &arr) {
        val = arr[0];
        size_t n = arr.size();
        ListNode *node = this;
        for (size_t i = 1; i < n; i++) {
            node->next = new ListNode(arr[i]);
            node = node->next;
        }
    }

    size_t length() {
        size_t res = 0;
        ListNode *node = this;
        while (node) {
            res++;
            node = node->next;
        }
        return res;
    }
};

class LinkList {
public:
    ListNode *head;
    size_t length;

    LinkList() {
        head = nullptr;
        length = 0;
    }

    LinkList(const vector<int> &arr) {
        head = new ListNode(arr[0]);
        ListNode *node = head;
        length = arr.size();
        for(size_t i = 1; i < length; i++) {
            node->next = new ListNode(arr[i]);
            node = node->next;
        }
    }

    LinkList(ListNode *ln) {
        head = new ListNode(ln->val);
        ListNode *node = head;
        length = 1;

        while (ln->next) {
            node->next = new ListNode(ln->next->val);
            node = node->next;
            ln = ln->next;
            length++;
        }
    }

    LinkList(const LinkList& ll) {
        head = new ListNode(ll.head);
        length = ll.length;
    }

    void print() {
        ListNode *node = head;
        while (node) {
            cout << node->val << endl;
            node = node->next;
        }
    }

    void append(int value) {
        ListNode *end = head;
        while (end->next) {
            end = end->next;
        }
        end->next = new ListNode(value);
        length++;
    }

    void append(const vector<int> &arr) {
        ListNode *end = head;
        while (end->next) {
            end = end->next;
        }

        size_t n = arr.size();
        length += n;
        for (size_t i = 0; i < n; i++) {
            end->next = new ListNode(arr[i]);
            end = end->next;
        }
    }

    void append(ListNode *ln) {
        ListNode *end = head;
        while (end->next) {
            end = end->next;
        }

        while (ln) {
            end->next = new ListNode(ln->val);
            end = end->next;
            ln = ln->next;
            length++;
        }
    }

    void append(const LinkList &ll) {
        append(ll.head);
    }

    void insert(size_t index, int value) {
        if (index == 0) {
            head = new ListNode(value, head);
            length++;
            return;
        }

        ListNode *node = head;
        for(size_t i = 1; i < index; i++) {
            node = node->next;
        }
        node->next = new ListNode(value, node->next);
        length++;
    }

    void insert(size_t index, ListNode *ln) {
        if (index == 0) {
            ListNode *head1 = head, *end;
            head = new ListNode(ln->val);
            end = head;
            length++;

            while (ln->next) {
                end->next = new ListNode(ln->next->val);
                ln = ln->next;
                end = end->next;
                length++;
            }
            end->next = head1;
        }

        ListNode *pre_node = head, *after_node;
        for (size_t i = 1; i < index; i++) {
            pre_node = pre_node->next;
        }
        after_node = pre_node->next;

        while (ln) {
            pre_node->next = new ListNode(ln->val);
            pre_node = pre_node->next;
            ln = ln->next;
            length++;
        }
        pre_node->next = after_node;
    }

    void insert(size_t index, const LinkList &ll) {
        insert(index, ll.head);
    }

    void insert(size_t index, const vector<int> &arr) {
        insert(index, new ListNode(arr));
    }

    void remove(size_t index) {
        if (index == 0) {
            ListNode *node = head->next;
            delete head;
            head = node;
        }

        ListNode *pre_node = head, *node, *after_node;
        for (size_t i = 1; i < index; i++) {
            pre_node = pre_node->next;
        }
        node = pre_node->next;
        after_node = node->next;
        pre_node->next = after_node;
        delete node;

        length--;
    }

    int get(size_t index) {
        ListNode *node = head;
        for (size_t i = 0; i < index; i++) {
            node = node->next;
        }
        return node->val;
    }

    void set(size_t index, int value) {
        ListNode *node = head;
        for (size_t i = 0; i < index; i++) {
            node = node->next;
        }
        node->val = value;
    }

    vector<int> to_vector() {
        ListNode *node = head;
        vector<int> res;
        while (node) {
            res.push_back(node->val);
            node = node->next;
        }
        return res;
    }
};