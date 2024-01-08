//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

/* Link list Node */
struct Node
{
    int data;
    struct Node* next;
};

void print(struct Node *Node)
{
    while (Node!=NULL)
    {
        cout << Node->data << " ";
        Node = Node->next;
    }
}


Node *newNode(int data)
{
    Node *temp = new Node;
    temp->data = data;
    temp->next = NULL;
    return temp;
}


// } Driver Code Ends
/*

The structure of linked list is the following

struct Node
{
    int data;
    Node* next;
};

*/

class Solution
{
public:
    Node *reverse(Node *root) 
    {
        Node *p = root, *pre = NULL;
        
        while(p) {
            Node *nxt = p->next;
            p->next = pre;
            pre = p, p = nxt;
        }
        
        return pre;
    }
    
    Node *merge(Node *l1, Node *l2) 
    {
        Node *dummy = newNode(0);
        Node *p = dummy;
        
        while(l1 and l2) 
        {
            if(l2->data <= l1->data) 
            {
                p->next = newNode(l2->data);
                l2 = l2->next;
            } else 
            {
                p->next = newNode(l1->data);
                l1 = l1->next;
            }
            
            p = p->next;
        }
        
        while(l1)
        {
            p->next = newNode(l1->data);
            l1 = l1->next;
            p = p->next;    
        }
        
        while(l2)
        {
            p->next = newNode(l2->data);
            l2 = l2->next;
            p = p->next;    
        }
        
        return dummy->next;
    }

    struct Node *mergeResult(Node *node1, Node *node2)
    {
        if(!node1 and !node2)
            return NULL;
            
        if(!node1)
            return reverse(node2);
            
        if(!node2)
            return reverse(node1);
            
        Node *res = merge(node1, node2);
        res = reverse(res);
        
        return res;
    }  
};


//{ Driver Code Starts.

int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        int nA;
        cin>>nA;
        int nB;
        cin>>nB;

        struct Node* headA=NULL;
        struct Node* tempA = headA;

        for(int i=0;i<nA;i++)
        {
            int ele;
            cin>>ele;
            if(headA==NULL)
            {
                headA=tempA=newNode(ele);

            }else{
                tempA->next = newNode(ele);
				tempA=tempA->next;
            }
        }

        struct Node* headB=NULL;
        struct Node* tempB = headB;


        for(int i=0;i<nB;i++)
        {
            int ele;
            cin>>ele;
            if(headB==NULL)
            {
                headB=tempB=newNode(ele);

            }else{
                tempB->next = newNode(ele);
				tempB=tempB->next;
            }
        }
        
        Solution ob;
        struct Node* result = ob.mergeResult(headA,headB);

        print(result);
        cout<<endl;


    }
}

// } Driver Code Ends