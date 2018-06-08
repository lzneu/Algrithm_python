
def printList(res):
    cur = res
    while cur is not None:
        print(cur.val)
        cur = cur.next

def genList(nums1, nums2):
    head1 = ListNode(nums1[0])
    cur = head1
    for num in nums1[1:]:
        # 尾插法
        cur.next = ListNode(num)
        cur = cur.next
    head2 = ListNode(nums2[0])
    cur = head2
    for num in nums2[1:]:
        # 尾插法
        cur.next = ListNode(num)
        cur = cur.next
    return head1, head2


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getMid(self, head):  # 至少两个元素
        slow = head
        fast = head
        pre = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        if fast is None:
            # 偶数个 直接切割
            pre.next = None
        else:  # 奇数个 后移切割
            pre = slow
            slow = slow.next
            pre.next = None
        return slow

    def reverse(self, head):  # 至少一个节点
        if head is None or head.next is None:
            return head
        pre = None
        cur = head
        while cur is not None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        # 思路： 切割找重点 反转 对比
        mHead = self.getMid(head)
        mHead = self.reverse(mHead)
        p = head
        q = mHead
        while q is not None and p is not None:
            if p.val == q.val:
                p = p.next
                q = q.next
            else:
                return False
        return True

nums1 = [1,2,2,1]
nums2 = [5,6,4]
head1, head2 = genList(nums1, nums2)
res = Solution().isPalindrome(head1)
# print(printList(res))
print(res)