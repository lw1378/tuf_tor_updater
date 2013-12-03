echo "Update repository metadata and update server metadata."
python repository_operator.py --update_repository -nd targets_files <<EOF
/home/laiwang/Documents/apache_Server/
EOF
echo "Update complete."
