using System;
using System.Collections.Generic;
using System.Text;

/*
 * Link: https://leetcode.com/problems/add-two-numbers/
 * Topic: Algorithms
 * Difficulty: Easy
 */

/*
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

namespace Into1
{
    public class Solution
    {
        public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
        {
            int carry = 0;
            int nextInt;
            ListNode ans = new ListNode(); //Listnode to build
            ListNode temp = ans; //Keep track of start of ans

            while ((l1.next != null) && (l2.next != null)) // If one list is longer than the other, go to the end of the shorter one.
            {
                nextInt = l1.val + l2.val + carry;

                if (nextInt >= 10)
                {
                    nextInt = nextInt -= 10; // Get the second digit
                    carry = 1;

                }
                else
                {
                    carry = 0;
                }

                ListNode nextNode = new ListNode(nextInt, null);
                ans.next = nextNode;
                ans = ans.next;

                l1 = l1.next;
                l2 = l2.next;
            }

            // One more time to get the last one
            nextInt = l1.val + l2.val + carry;

            if (nextInt >= 10)
            {
                nextInt = nextInt -= 10; // Get the second digit
                carry = 1;

            }
            else
            {
                carry = 0;
            }

            ListNode newNode = new ListNode(nextInt, null);
            ans.next = newNode;
            ans = ans.next;

            // Now add the remainder of the longer list
            if (l1.next != null)
            {
                l1 = l1.next;
                if (carry == 1)
                {
                    l1 = CheckCarry(l1);
                }

                ans.next = l1;

            }
            else if (l2.next != null) // Else if in case both lists are done
            {
                l2 = l2.next;
                if (carry == 1)
                {
                    l2 = CheckCarry(l2);
                }
                ans.next = l2;

            }
            else if (carry == 1) // both are done at the same time, but final number was 10 
            {
                ListNode finalNode = new ListNode(1, null);
                ans.next = finalNode;
            }

            return temp.next;
        }

        public ListNode CheckCarry(ListNode l1)
        {
            l1.val += 1;

            if (l1.val >= 10 && (l1.next != null))
            {
                l1.val -= 10; // Get first digit

                l1.next = CheckCarry(l1.next);

            }
            else if (l1.val >= 10) // Last one
            {
                l1.val = 0;

                ListNode finalNode = new ListNode(1, null);
                l1.next = finalNode;
            }

            return l1;
        }
    }
}
