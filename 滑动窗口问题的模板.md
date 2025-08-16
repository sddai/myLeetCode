# 滑动窗口问题的通用模板
```cpp
int left = 0, right = 0;

while (left < right && right < s.size()) {
    // 增大窗口
    window.add(s[right]);
    right++;
    
    while (window needs shrink) {
        // 缩小窗口
        window.remove(s[left]);
        left++;
    }
}
```

## 注意事项
1. 总体上是两层while循环，但是时间复杂度仍为O(N)；
2. 收缩窗口的过程是一个while而不是if，因为只要满足收缩条件就会一直进行窗口收缩。