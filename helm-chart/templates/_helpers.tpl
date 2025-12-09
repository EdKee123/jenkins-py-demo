{{/* Generate full name for resources */}}
{{- define "jenkins-py-demo.fullname" -}}
{{- printf "%s" .Chart.Name -}}
{{- end -}}
