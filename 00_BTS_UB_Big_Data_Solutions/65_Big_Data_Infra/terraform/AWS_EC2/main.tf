resource "aws_instance" "myInstance" {
  ami           = "ami-042e8287309f5df03"
  instance_type = "t2.micro"
  user_data     = <<-EOF
                  #!/bin/bash
                  sudo apt-get install httpd -y
                  echo "<p> My Instance! </p>" >> /var/www/html/index.html
                  sudo systemctl enable httpd
                  sudo systemctl start httpd
                  EOF
}

output "DNS" {
  value = aws_instance.myInstance.public_dns
}
