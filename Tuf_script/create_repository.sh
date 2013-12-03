echo "Generate new repository and update the server and client."
python repository_operator.py --generate_repository -nd targets_files <<EOF
/home/laiwang/Documents/apache_Server/
/home/laiwang/Documents/repy_tuf/client/
EOF
echo "Repository generation complete."
