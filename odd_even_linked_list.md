#### 奇偶链表

[题目链接](https://leetcode-cn.com/problems/odd-even-linked-list)

> 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
>
> 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
>
> **示例 1:**
>
> ```
> 输入: 1->2->3->4->5->NULL
> 输出: 1->3->5->2->4->NULL
> ```
>
> **示例 2:**
>
> ```
> 输入: 2->1->3->5->6->4->7->NULL 
> 输出: 2->3->6->7->1->5->4->NULL
> ```
>
> **说明:**
>
> - 应当保持奇数节点和偶数节点的相对顺序。
> - 链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。

**简单思路**

假设链表如下图所示

![](https://i.loli.net/2019/05/08/5cd2a80c27c9a.png)

那么，定义奇数链表指针`odd`和偶数链表指针`even`，分别指向第一个节点和第二个节点，每次奇数链表指针`odd`先往后跳两个节点，连接到下一个奇数节点，随后偶数链表指针`even`往后跳两个节点，连接到下一个偶数节点。过程如下，

第一次：

![](https://i.loli.net/2019/05/08/5cd2a80c413b4.png)

第二次：

![](https://i.loli.net/2019/05/08/5cd2a80c51a2f.png)

第三次：

![](https://i.loli.net/2019/05/08/5cd2a80c52835.png)

此时，奇数链表`odd_head`和偶数链表`even_head`如下所示。

![](https://i.loli.net/2019/05/08/5cd2a80c3e130.png)

最后将`even_head`连接到`odd_head`之后即可，注意一些特殊情况的判断。时间复杂度$O(n)$，空间复杂度$O(1)$，执行时间72ms

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        odd_head, odd = head, head
        even_head, even = head.next, head.next
        
        while (odd and odd.next and odd.next.next) or (even and even.next):
            if odd.next and odd.next.next:
                odd.next = odd.next.next
                odd = odd.next

            if even.next:
                even.next = even.next.next
                even = even.next
        
        odd.next = even_head
        
        return odd_head
```

