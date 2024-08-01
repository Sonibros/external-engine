import subprocess

# Call the extengine.sh script using subprocess.run()
subprocess.run(['./extengine.sh'])

# Alternative using shell=True (not recommended for security reasons)
# subprocess.run('sh extengine.sh', shell=True)

print("extengine.sh script executed successfully!")
