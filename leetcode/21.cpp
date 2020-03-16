// 21. Merge Two Sorted Lists

// Solution 1 - Beat 99.67%
// Using Linked List
/*
 * Definition for singly-linked list.
 */
#include <iostream>

using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode * merged = new ListNode(0);
        ListNode * head = merged;
        while(l1 != NULL || l2 != NULL){
            if(l1 != NULL && l2 != NULL){
                if(l1->val <= l2->val){
                    ListNode * tmp = new ListNode(l1->val);
                    
                    merged->next= tmp;
                    l1 = l1->next;
                }else{
                    ListNode * tmp = new ListNode(l2->val);
                    merged->next = tmp;
                    l2 = l2->next;
                }
            }else if(l1==NULL && l2 !=NULL){
                ListNode * tmp = new ListNode(l2->val);
                merged->next = tmp;
                l2 = l2->next;                
            }else{
                ListNode * tmp = new ListNode(l1->val);
                merged->next = tmp;
                l1 = l1->next;                
            }
            merged = merged->next;
        }
        return head->next;
    }
};

int main(){
	Solution sol;
	ListNode * a = new ListNode(1);
	ListNode * b = new ListNode(2);
	ListNode * merged = sol.mergeTwoLists(a,b);
	while(merged!=NULL){
		cout << merged->val << endl;
		merged = merged->next;
	}	

	return 0;

}
