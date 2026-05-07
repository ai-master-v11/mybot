import os
import subprocess

def deploy_project():
    print("🚀 Project 07: 2030 Vision Deployment Starting...")
    
    try:
        # ১. গিট ইনিশিয়ালাইজ করা (যদি আগে না করা থাকে)
        subprocess.run(["git", "add", "."], check=True)
        
        # ২. পরিবর্তনের নাম দেওয়া (Commit Message)
        commit_message = "Update: Elite 2030 Modules Integrated"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # ৩. মেইন ব্রাঞ্চে কোড পুশ করা
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        print("\n✅ Success! Your 26 files are now syncing with Render.")
        print("🔗 Check Render Dashboard to see the Live Logic.")
        
    except Exception as e:
        print(f"❌ Error during deployment: {e}")

if __name__ == "__main__":
    deploy_project()
