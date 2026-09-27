# কিছু কাল্পনিক ট্রেনিং ডাটা
# x = ঘরের সাইজ (শ বর্গফুটে), y = ঘরের দাম (লাখ টাকায়)
x_train = [1.0, 2.0, 3.0, 4.0]
y_train = [2.0, 4.0, 5.0, 4.0]

m_data = len(x_train) # মোট ট্রেনিং ডাটার সংখ্যা (m)

# ১. প্যারামিটার দুটির প্রাথমিক মান (w_0 এবং w_1) ধরে নেওয়া
w0 = 0.0 # ইন্টারসেপ্ট (c এর মতো)
w1 = 0.0 # স্লোপ (m এর মতো)

learning_rate = 0.01 # লার্নিং রেট বা স্টেপ সাইজ (alpha)
epochs = 50      # কতবার লুপটি চলবে (Iterations)

# গ্র্যাডিয়েন্ট ডিসেন্ট লুপ
for epoch in range(epochs):
    dw0 = 0.0
    dw1 = 0.0
    cost = 0.0
    
    # প্রতিটা ট্রেনিং ডাটার জন্য লুপ চালিয়ে এরর এবং ডেরিভেটিভ বের করা
    for i in range(m_data):
        x_i = x_train[i]
        y_i = y_train[i]
        
        # প্রেডিকটেড মান: h_w(x) = w0 + w1 * x
        h_i = w0 + w1 * x_i
        
        # স্কোয়ার্ড এরর যোগ করা
        cost += (h_i - y_i) ** 2
        
        # বইয়ের দেওয়া ডেরিভেটিভের সূত্র অনুযায়ী গ্রেডিয়েন্ট হিসাব করা
        # d/dw0 J(w0, w1) = (1/m) * sum(h_i - y_i)
        dw0 += (h_i - y_i)
        
        # d/dw1 J(w0, w1) = (1/m) * sum((h_i - y_i) * x_i)
        dw1 += (h_i - y_i) * x_i
        
        
    # ফাইনাল গড় কস্ট (Cost Function J) হিসাব
    cost = cost / (2 * m_data)
    
    # গড়ের জন্য m_data দিয়ে ভাগ করা
    dw0 = dw0 / m_data
    dw1 = dw1 / m_data
    
    # ২. একসাথে w0 এবং w1 এর মান আপডেট করা (Gradient Descent Update Rule)
    w0 = w0 - learning_rate * dw0
    w1 = w1 - learning_rate * dw1
    
    # প্রতি ১০০ ইটারেশনে কস্ট বা এরর প্রিন্ট করে দেখা
    if epoch % 100 == 0:
        pass
    print(f"w0-> {w0:.4f}   w1-> {w1:.4f}   cost->{cost:.4f}")

#print("\n--- ফিনাল রেজাল্ট ---")
#print(f"অপ্টিমাইজড w0 (Intercept): {w0:.4f}")
#print(f"অপ্টিমাইজড w1 (Slope): {w1:.4f}")

# নতুন কোনো ডেটার জন্য প্রেডিকশন করে দেখা
test_x = 2.5
predicted_y = w0 + w1 * test_x
#print(f"যদি ঘরের সাইজ {test_x} হয়, তবে প্রেডিক্টেড দাম: {predicted_y:.4f} লাখ টাকা")